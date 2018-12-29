# Denon AH-C452K
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -11.9; 23 -11.8; 25 -11.7; 28 -11.5; 31 -11.3; 34 -11.1; 37 -11.0; 41 -10.8; 45 -10.6; 49 -10.4; 54 -10.2; 60 -10.0; 66 -9.9; 72 -9.7; 79 -9.5; 87 -9.3; 96 -9.0; 106 -8.6; 116 -8.3; 128 -8.0; 141 -7.6; 155 -7.2; 170 -6.7; 187 -6.1; 206 -5.4; 227 -4.9; 249 -5.3; 274 -4.7; 302 -3.9; 332 -3.2; 365 -2.5; 402 -1.9; 442 -1.4; 486 -0.9; 535 -0.4; 588 0.1; 647 0.5; 712 0.7; 783 0.8; 861 0.7; 947 0.2; 1042 -0.3; 1146 -0.8; 1261 -0.3; 1387 -0.7; 1526 -2.6; 1678 -3.9; 1846 -4.4; 2031 -4.8; 2234 -5.4; 2457 -6.1; 2703 -7.2; 2973 -6.9; 3270 -4.4; 3597 -1.8; 3957 -2.0; 4353 -4.3; 4788 -6.8; 5267 -9.7; 5793 -11.8; 6373 -6.7; 7010 -4.2; 7711 -5.3; 8482 -9.0; 9330 -8.3; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C452K GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C452K ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.21 | -11.5 dB |
| Peaking | 155 Hz   | 0.74 | -3.3 dB  |
| Peaking | 2413 Hz  | 2.03 | -5.8 dB  |
| Peaking | 6073 Hz  | 1.27 | -8.8 dB  |
| Peaking | 24000 Hz | 2.37 | -6.2 dB  |
| Peaking | 3857 Hz  | 6.65 | 3.4 dB   |
| Peaking | 5661 Hz  | 5.57 | -5.0 dB  |
| Peaking | 6959 Hz  | 3.06 | 5.8 dB   |
| Peaking | 9050 Hz  | 3.02 | -10.5 dB |
| Peaking | 10329 Hz | 2.13 | 5.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C452K/Denon%20AH-C452K.png)