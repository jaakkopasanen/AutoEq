# Shure SRH940
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 5.0; 34 4.2; 37 3.6; 41 2.8; 45 2.2; 49 1.7; 54 1.3; 60 0.9; 66 0.8; 72 1.5; 79 2.7; 87 2.8; 96 1.2; 106 0.3; 116 0.5; 128 0.8; 141 -0.0; 155 -0.3; 170 -0.2; 187 -1.6; 206 -2.2; 227 -2.6; 249 -2.9; 274 -2.8; 302 -2.7; 332 -3.9; 365 -2.8; 402 -2.2; 442 -1.9; 486 -1.6; 535 -1.3; 588 -0.9; 647 -0.6; 712 -0.4; 783 0.0; 861 0.3; 947 -0.1; 1042 0.1; 1146 -0.0; 1261 -0.3; 1387 -1.0; 1526 -1.6; 1678 -2.1; 1846 -2.0; 2031 -1.9; 2234 -1.7; 2457 -0.2; 2703 -0.4; 2973 -0.4; 3270 -0.9; 3597 -1.5; 3957 -2.5; 4353 -2.8; 4788 -2.1; 5267 0.9; 5793 3.1; 6373 3.7; 7010 2.5; 7711 -0.5; 8482 -7.3; 9330 -9.8; 10263 -1.9; 11289 0.0; 12418 0.0; 13660 -1.2; 15026 -3.2; 16529 -1.7; 18182 -3.5; 20000 -7.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SRH940 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH940 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.31 | 7.5 dB   |
| Peaking | 305 Hz   | 1.26 | -3.5 dB  |
| Peaking | 5640 Hz  | 0.68 | -4.3 dB  |
| Peaking | 6415 Hz  | 2.19 | 9.0 dB   |
| Peaking | 9003 Hz  | 5.32 | -10.6 dB |
| Peaking | 57 Hz    | 2.11 | -1.4 dB  |
| Peaking | 82 Hz    | 5.04 | 2.5 dB   |
| Peaking | 1827 Hz  | 3.01 | -1.7 dB  |
| Peaking | 2763 Hz  | 3.7  | 1.7 dB   |
| Peaking | 11028 Hz | 6.94 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SRH940/Shure%20SRH940.png)