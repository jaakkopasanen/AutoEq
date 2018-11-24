# Apple Stock Bud New

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 5.4; 155 4.2; 170 3.1; 187 2.2; 206 1.7; 227 1.3; 249 1.0; 274 0.8; 302 0.7; 332 0.7; 365 0.7; 402 0.8; 442 1.2; 486 0.8; 535 1.0; 588 0.6; 647 0.5; 712 0.4; 783 0.3; 861 0.2; 947 -0.0; 1042 -0.1; 1146 -0.2; 1261 -0.3; 1387 -0.7; 1526 -1.4; 1678 -2.1; 1846 -2.7; 2031 -3.6; 2234 -5.1; 2457 -7.2; 2703 -9.0; 2973 -9.3; 3270 -7.6; 3597 -5.2; 3957 -4.5; 4353 -5.7; 4788 -6.2; 5267 -5.8; 5793 -6.2; 6373 -6.1; 7010 -5.4; 7711 -4.8; 8482 -4.5; 9330 -2.8; 10263 -0.2; 11289 0.0; 12418 -0.0; 13660 -3.6; 15026 -4.6; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Apple Stock Bud New GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple Stock Bud New ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.32 | 6.7 dB  |
| Peaking | 902 Hz   | 1.45 | 0.4 dB  |
| Peaking | 2798 Hz  | 1.98 | -8.6 dB |
| Peaking | 6108 Hz  | 1.29 | -5.9 dB |
| Peaking | 14684 Hz | 5.1  | -5.3 dB |
| Peaking | 17 Hz    | 2.76 | 1.0 dB  |
| Peaking | 132 Hz   | 3.07 | 2.0 dB  |
| Peaking | 224 Hz   | 1.63 | -1.3 dB |
| Peaking | 8697 Hz  | 4.78 | -1.9 dB |
| Peaking | 10771 Hz | 3.04 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Apple%20Stock%20Bud%20New/Apple%20Stock%20Bud%20New.png)