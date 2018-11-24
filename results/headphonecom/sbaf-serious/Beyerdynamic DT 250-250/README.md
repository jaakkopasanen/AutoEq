# Beyerdynamic DT 250-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.5; 87 4.7; 96 4.1; 106 3.6; 116 3.1; 128 2.4; 141 1.8; 155 1.7; 170 1.5; 187 0.9; 206 0.5; 227 0.2; 249 0.2; 274 0.2; 302 0.1; 332 -0.1; 365 -0.2; 402 -0.1; 442 0.2; 486 0.6; 535 0.8; 588 1.1; 647 1.0; 712 0.8; 783 0.6; 861 0.4; 947 0.1; 1042 1.9; 1146 2.5; 1261 1.7; 1387 0.8; 1526 -1.0; 1678 -2.0; 1846 -2.0; 2031 -1.9; 2234 -2.0; 2457 -2.7; 2703 -2.7; 2973 -1.4; 3270 -0.6; 3597 -1.5; 3957 -1.9; 4353 -1.9; 4788 -0.9; 5267 2.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -4.0; 10263 -4.7; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.44 | 6.7 dB  |
| Peaking | 1160 Hz | 2.89 | 3.7 dB  |
| Peaking | 2788 Hz | 0.56 | -2.6 dB |
| Peaking | 6082 Hz | 3.47 | 8.1 dB  |
| Peaking | 9947 Hz | 5.5  | -5.7 dB |
| Peaking | 76 Hz   | 4.69 | 1.0 dB  |
| Peaking | 617 Hz  | 4.02 | 1.3 dB  |
| Peaking | 3251 Hz | 4.04 | 3.7 dB  |
| Peaking | 3365 Hz | 1.75 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)