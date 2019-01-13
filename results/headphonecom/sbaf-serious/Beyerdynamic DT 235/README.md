# Beyerdynamic DT 235
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 5.7; 141 5.1; 155 5.0; 170 5.3; 187 5.7; 206 5.3; 227 5.2; 249 4.9; 274 4.6; 302 4.2; 332 3.9; 365 3.4; 402 3.0; 442 3.0; 486 2.4; 535 2.1; 588 1.8; 647 1.5; 712 0.6; 783 -0.7; 861 -1.3; 947 -0.8; 1042 0.4; 1146 1.9; 1261 3.1; 1387 3.2; 1526 1.8; 1678 -1.3; 1846 -0.8; 2031 2.2; 2234 3.1; 2457 4.3; 2703 5.9; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 1.9; 4788 -5.3; 5267 -1.0; 5793 2.6; 6373 1.4; 7010 -1.4; 7711 -3.7; 8482 -1.1; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -5.8; 15026 -6.7; 16529 -2.5; 18182 0.0; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 13 Hz    | 0.25 | 5.6 dB   |
| Peaking | 103 Hz   | 0.48 | 4.0 dB   |
| Peaking | 274 Hz   | 0.91 | 2.6 dB   |
| Peaking | 3081 Hz  | 2.16 | 7.0 dB   |
| Peaking | 14533 Hz | 2.93 | -7.7 dB  |
| Peaking | 872 Hz   | 4.47 | -2.5 dB  |
| Peaking | 1290 Hz  | 6.23 | 3.1 dB   |
| Peaking | 4887 Hz  | 7.3  | -10.3 dB |
| Peaking | 6101 Hz  | 1.1  | 4.3 dB   |
| Peaking | 7516 Hz  | 3.68 | -7.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)