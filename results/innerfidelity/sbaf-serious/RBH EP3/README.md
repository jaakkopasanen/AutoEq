# RBH EP3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 -15.0; 23 -14.9; 25 -14.8; 28 -14.7; 31 -14.5; 34 -14.3; 37 -14.1; 41 -13.9; 45 -13.7; 49 -13.5; 54 -13.3; 60 -13.1; 66 -12.9; 72 -12.8; 79 -12.6; 87 -12.5; 96 -12.3; 106 -12.0; 116 -11.6; 128 -11.3; 141 -11.0; 155 -10.6; 170 -10.1; 187 -9.6; 206 -9.0; 227 -8.3; 249 -7.8; 274 -7.1; 302 -6.5; 332 -5.8; 365 -5.1; 402 -4.4; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.5; 647 -0.9; 712 -0.5; 783 0.0; 861 0.0; 947 0.1; 1042 0.0; 1146 0.1; 1261 -0.8; 1387 -2.3; 1526 -3.2; 1678 -3.8; 1846 -4.0; 2031 -4.1; 2234 -4.1; 2457 -3.5; 2703 -2.7; 2973 -0.8; 3270 1.4; 3597 2.2; 3957 1.1; 4353 -2.4; 4788 -5.8; 5267 -9.6; 5793 -6.4; 6373 -0.5; 7010 2.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -2.8; 16529 -1.2; 18182 0.0; 20000 -2.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`RBH EP3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-23**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.15 | -14.6 dB |
| Peaking | 181 Hz   | 0.66 | -4.5 dB  |
| Peaking | 1970 Hz  | 2.44 | -4.5 dB  |
| Peaking | 5363 Hz  | 5.03 | -10.9 dB |
| Peaking | 6871 Hz  | 4.34 | 3.1 dB   |
| Peaking | 868 Hz   | 1.33 | 2.4 dB   |
| Peaking | 1309 Hz  | 0.24 | -1.0 dB  |
| Peaking | 2657 Hz  | 6.18 | -1.3 dB  |
| Peaking | 3531 Hz  | 4.07 | 4.4 dB   |
| Peaking | 15517 Hz | 5.26 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP3/RBH%20EP3.png)