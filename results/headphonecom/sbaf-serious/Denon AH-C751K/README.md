# Denon AH-C751K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 21 -8.1; 23 -8.3; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.6; 37 -8.5; 41 -8.4; 45 -8.6; 49 -8.8; 54 -8.9; 60 -8.9; 66 -8.9; 72 -8.9; 79 -8.8; 87 -8.7; 96 -8.6; 106 -8.3; 116 -8.0; 128 -7.6; 141 -7.0; 155 -7.9; 170 -7.9; 187 -7.3; 206 -6.7; 227 -6.1; 249 -5.5; 274 -4.9; 302 -4.2; 332 -3.5; 365 -2.8; 402 -2.2; 442 -1.6; 486 -1.1; 535 -0.6; 588 -0.1; 647 0.3; 712 0.5; 783 0.7; 861 0.5; 947 0.2; 1042 -0.3; 1146 -0.8; 1261 -1.4; 1387 -2.4; 1526 -3.6; 1678 -4.4; 1846 -5.4; 2031 -6.5; 2234 -7.0; 2457 -8.0; 2703 -9.2; 2973 -9.4; 3270 -6.5; 3597 -3.9; 3957 -4.0; 4353 -6.1; 4788 -8.1; 5267 -10.1; 5793 -11.4; 6373 -8.7; 7010 -7.4; 7711 -9.4; 8482 -11.1; 9330 -7.0; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.8; 16529 -0.3; 18182 0.0; 20000 -2.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C751K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-7**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C751K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 44 Hz    | 0.3  | -9.1 dB  |
| Peaking | 188 Hz   | 1.14 | -3.7 dB  |
| Peaking | 2493 Hz  | 1.69 | -7.6 dB  |
| Peaking | 6496 Hz  | 1.13 | -10.0 dB |
| Peaking | 20961 Hz | 2.37 | -8.1 dB  |
| Peaking | 3862 Hz  | 4.44 | 4.0 dB   |
| Peaking | 5974 Hz  | 1.03 | -3.5 dB  |
| Peaking | 6876 Hz  | 3.78 | 6.6 dB   |
| Peaking | 8791 Hz  | 3.42 | -7.2 dB  |
| Peaking | 10242 Hz | 2.13 | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C751K/Denon%20AH-C751K.png)