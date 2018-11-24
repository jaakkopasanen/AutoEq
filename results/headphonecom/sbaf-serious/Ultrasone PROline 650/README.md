# Ultrasone PROline 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.6; 28 -1.2; 31 -1.6; 34 -2.0; 37 -2.4; 41 -2.4; 45 -1.8; 49 -0.2; 54 0.9; 60 -1.1; 66 -2.7; 72 -3.7; 79 -3.9; 87 -3.1; 96 -3.0; 106 -3.0; 116 -2.0; 128 -1.8; 141 -2.0; 155 -1.4; 170 -0.4; 187 0.1; 206 1.3; 227 2.3; 249 3.4; 274 4.6; 302 4.9; 332 4.4; 365 3.7; 402 2.7; 442 2.1; 486 2.7; 535 5.7; 588 2.8; 647 1.7; 712 1.5; 783 1.2; 861 0.7; 947 0.4; 1042 -0.1; 1146 -0.2; 1261 -0.2; 1387 -0.8; 1526 -1.9; 1678 -2.8; 1846 -2.7; 2031 -1.4; 2234 4.5; 2457 4.2; 2703 -1.4; 2973 -1.4; 3270 -2.1; 3597 -3.6; 3957 -3.9; 4353 -3.1; 4788 -0.3; 5267 -0.5; 5793 3.6; 6373 -0.5; 7010 0.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.9; 15026 -7.5; 16529 -6.8; 18182 -0.3; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 650 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 92 Hz    |  0.88 | -3.5 dB |
| Peaking | 295 Hz   |  1.74 | 5.4 dB  |
| Peaking | 536 Hz   |  5.42 | 4.7 dB  |
| Peaking | 3818 Hz  |  4.26 | -4.5 dB |
| Peaking | 15713 Hz |  3.38 | -9.5 dB |
| Peaking | 46 Hz    |  1.48 | -2.6 dB |
| Peaking | 52 Hz    |  4.18 | 4.8 dB  |
| Peaking | 2073 Hz  |  1.82 | -4.5 dB |
| Peaking | 2318 Hz  |  6.47 | 10.7 dB |
| Peaking | 5859 Hz  | 10.64 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20650/Ultrasone%20PROline%20650.png)