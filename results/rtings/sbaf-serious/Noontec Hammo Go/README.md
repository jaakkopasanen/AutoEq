# Noontec Hammo Go

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.2; 41 4.3; 45 3.5; 49 3.1; 54 2.6; 60 1.6; 66 1.1; 72 0.7; 79 0.3; 87 -0.3; 96 -0.9; 106 -1.6; 116 -2.2; 128 -2.5; 141 -2.4; 155 -2.4; 170 -2.9; 187 -3.5; 206 -4.0; 227 -4.2; 249 -4.1; 274 -3.6; 302 -3.2; 332 -3.3; 365 -3.2; 402 -2.9; 442 -1.0; 486 -0.2; 535 0.2; 588 0.7; 647 1.4; 712 0.5; 783 0.4; 861 -0.3; 947 -0.5; 1042 0.4; 1146 1.7; 1261 2.4; 1387 2.8; 1526 2.8; 1678 3.2; 1846 3.7; 2031 3.8; 2234 3.4; 2457 2.6; 2703 2.6; 2973 2.4; 3270 1.3; 3597 -2.0; 3957 0.1; 4353 0.7; 4788 -2.2; 5267 -0.9; 5793 -0.6; 6373 1.9; 7010 0.7; 7711 -5.3; 8482 -9.0; 9330 -5.8; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -2.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noontec Hammo Go GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontec Hammo Go ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.67 | 6.4 dB   |
| Peaking | 122 Hz   | 1.11 | -2.1 dB  |
| Peaking | 254 Hz   | 1.22 | -4.0 dB  |
| Peaking | 1867 Hz  | 1.27 | 4.0 dB   |
| Peaking | 8513 Hz  | 5.14 | -10.3 dB |
| Peaking | 383 Hz   | 7.62 | -1.5 dB  |
| Peaking | 613 Hz   | 4.38 | 1.6 dB   |
| Peaking | 4900 Hz  | 5.41 | -2.3 dB  |
| Peaking | 6640 Hz  | 9.44 | 4.1 dB   |
| Peaking | 17649 Hz | 4.86 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Noontec%20Hammo%20Go/Noontec%20Hammo%20Go.png)