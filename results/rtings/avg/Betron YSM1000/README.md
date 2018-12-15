# Betron YSM1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.1; 28 -3.2; 31 -3.3; 34 -3.4; 37 -3.5; 41 -3.6; 45 -3.8; 49 -3.9; 54 -4.2; 60 -4.7; 66 -5.2; 72 -5.7; 79 -6.2; 87 -6.8; 96 -7.4; 106 -8.1; 116 -8.7; 128 -9.3; 141 -9.8; 155 -10.1; 170 -10.2; 187 -10.3; 206 -10.3; 227 -10.2; 249 -10.0; 274 -9.6; 302 -9.1; 332 -8.5; 365 -7.9; 402 -7.2; 442 -6.4; 486 -5.6; 535 -4.6; 588 -3.6; 647 -2.6; 712 -1.7; 783 -0.9; 861 -0.2; 947 -0.0; 1042 0.1; 1146 0.3; 1261 1.0; 1387 1.7; 1526 0.1; 1678 -1.8; 1846 -1.8; 2031 -1.0; 2234 0.4; 2457 1.7; 2703 2.1; 2973 1.2; 3270 -0.1; 3597 -1.9; 3957 -3.6; 4353 -5.9; 4788 -8.1; 5267 -8.5; 5793 -3.7; 6373 0.2; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.3; 16529 -2.9; 18182 -2.3; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Betron YSM1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Betron YSM1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 35 Hz    | 0.15 | -2.6 dB  |
| Peaking | 157 Hz   | 0.68 | -6.8 dB  |
| Peaking | 340 Hz   | 0.82 | -5.9 dB  |
| Peaking | 1504 Hz  | 0.15 | 1.4 dB   |
| Peaking | 4872 Hz  | 3.21 | -10.5 dB |
| Peaking | 1436 Hz  | 2.37 | 4.0 dB   |
| Peaking | 1691 Hz  | 2.04 | -5.0 dB  |
| Peaking | 2603 Hz  | 4.18 | 2.6 dB   |
| Peaking | 6802 Hz  | 8.09 | 3.7 dB   |
| Peaking | 20678 Hz | 0.74 | -5.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Betron%20YSM1000/Betron%20YSM1000.png)