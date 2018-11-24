# Sony MDR-Q68LW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.7; 66 4.3; 72 3.0; 79 2.0; 87 1.2; 96 0.5; 106 0.0; 116 -0.1; 128 -0.4; 141 -0.6; 155 -0.6; 170 -0.7; 187 -0.6; 206 -0.5; 227 -0.5; 249 -0.3; 274 0.1; 302 0.4; 332 0.5; 365 0.7; 402 0.8; 442 0.9; 486 1.0; 535 1.2; 588 1.2; 647 1.2; 712 1.1; 783 0.9; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -1.1; 1387 -2.2; 1526 -3.7; 1678 -4.6; 1846 -5.4; 2031 -5.4; 2234 -5.3; 2457 -5.1; 2703 -4.7; 2973 -3.4; 3270 -1.7; 3597 -1.6; 3957 -3.9; 4353 -2.9; 4788 0.7; 5267 4.1; 5793 6.0; 6373 4.7; 7010 1.0; 7711 -1.7; 8482 -0.1; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-Q68LW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Q68LW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.86 | 7.1 dB  |
| Peaking | 758 Hz  | 1.05 | 1.8 dB  |
| Peaking | 2076 Hz | 1.2  | -6.1 dB |
| Peaking | 4176 Hz | 6.5  | -3.7 dB |
| Peaking | 5771 Hz | 3.92 | 7.4 dB  |
| Peaking | 40 Hz   | 3.25 | -1.4 dB |
| Peaking | 58 Hz   | 2.9  | 2.5 dB  |
| Peaking | 131 Hz  | 1.09 | -1.5 dB |
| Peaking | 6551 Hz | 8.57 | 1.8 dB  |
| Peaking | 7594 Hz | 6.13 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Q68LW/Sony%20MDR-Q68LW.png)