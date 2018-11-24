# Ultrasone PROline 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 3.9; 402 0.9; 442 -0.8; 486 -1.6; 535 -1.4; 588 -1.6; 647 0.2; 712 0.4; 783 0.4; 861 0.1; 947 0.1; 1042 -0.1; 1146 -0.0; 1261 0.2; 1387 0.5; 1526 0.1; 1678 0.5; 1846 2.4; 2031 2.3; 2234 1.4; 2457 -1.2; 2703 1.7; 2973 4.0; 3270 3.2; 3597 1.6; 3957 4.3; 4353 3.3; 4788 0.4; 5267 0.4; 5793 2.9; 6373 5.5; 7010 2.5; 7711 0.2; 8482 -2.6; 9330 -4.5; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -2.4; 18182 -2.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone PROline 550 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone PROline 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 67 Hz    | 0.22 | 6.7 dB  |
| Peaking | 3503 Hz  | 1.84 | 3.3 dB  |
| Peaking | 6349 Hz  | 6.6  | 6.0 dB  |
| Peaking | 9099 Hz  | 5.28 | -5.1 dB |
| Peaking | 17503 Hz | 3.09 | -3.7 dB |
| Peaking | 20 Hz    | 1.35 | 1.9 dB  |
| Peaking | 166 Hz   | 0.09 | -0.9 dB |
| Peaking | 353 Hz   | 1.03 | 6.6 dB  |
| Peaking | 459 Hz   | 1.77 | -7.9 dB |
| Peaking | 1928 Hz  | 6.8  | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20PROline%20550/Ultrasone%20PROline%20550.png)