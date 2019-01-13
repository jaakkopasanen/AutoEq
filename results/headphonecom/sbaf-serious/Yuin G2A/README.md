# Yuin G2A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.4; 49 4.6; 54 3.7; 60 2.8; 66 2.0; 72 1.5; 79 1.2; 87 0.4; 96 -0.2; 106 -0.7; 116 -1.1; 128 -1.5; 141 -2.0; 155 -2.2; 170 -2.1; 187 -2.1; 206 -1.9; 227 -1.9; 249 -1.7; 274 -1.8; 302 -1.5; 332 -1.3; 365 -1.1; 402 -0.7; 442 -0.7; 486 -0.3; 535 -0.2; 588 0.1; 647 0.3; 712 0.2; 783 0.4; 861 0.3; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.6; 1387 -1.3; 1526 -1.9; 1678 -3.0; 1846 -3.9; 2031 -4.6; 2234 -4.4; 2457 -3.2; 2703 -0.8; 2973 2.2; 3270 4.7; 3597 5.9; 3957 1.8; 4353 -4.4; 4788 -6.7; 5267 -4.0; 5793 2.5; 6373 5.5; 7010 2.5; 7711 -1.3; 8482 -5.1; 9330 -6.2; 10263 -2.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Yuin G2A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin G2A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.14 | 7.1 dB   |
| Peaking | 2267 Hz  | 1.1  | -13.7 dB |
| Peaking | 3665 Hz  | 0.7  | 16.1 dB  |
| Peaking | 4645 Hz  | 3.56 | -17.8 dB |
| Peaking | 9085 Hz  | 3.08 | -10.3 dB |
| Peaking | 53 Hz    | 1.71 | 1.6 dB   |
| Peaking | 173 Hz   | 0.81 | -2.5 dB  |
| Peaking | 5326 Hz  | 9.34 | -3.7 dB  |
| Peaking | 6235 Hz  | 6.3  | 4.4 dB   |
| Peaking | 19461 Hz | 0.19 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Yuin%20G2A/Yuin%20G2A.png)