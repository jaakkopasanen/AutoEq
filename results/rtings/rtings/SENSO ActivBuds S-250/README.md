# SENSO ActivBuds S-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.0; 28 -0.4; 31 -0.8; 34 -1.2; 37 -1.5; 41 -1.9; 45 -2.3; 49 -2.6; 54 -3.2; 60 -4.1; 66 -4.9; 72 -5.6; 79 -6.5; 87 -7.5; 96 -8.5; 106 -9.7; 116 -10.8; 128 -11.9; 141 -12.9; 155 -13.8; 170 -14.5; 187 -15.2; 206 -15.6; 227 -15.8; 249 -15.8; 274 -15.6; 302 -15.3; 332 -14.9; 365 -14.3; 402 -13.5; 442 -12.6; 486 -11.4; 535 -10.0; 588 -8.5; 647 -6.7; 712 -4.9; 783 -3.2; 861 -1.7; 947 -0.5; 1042 0.4; 1146 1.6; 1261 3.3; 1387 5.3; 1526 6.0; 1678 5.4; 1846 2.2; 2031 0.5; 2234 2.2; 2457 5.3; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SENSO ActivBuds S-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SENSO ActivBuds S-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 15 Hz   | 1.14 | 1.8 dB   |
| Peaking | 146 Hz  | 0.74 | -5.0 dB  |
| Peaking | 302 Hz  | 0.49 | -13.9 dB |
| Peaking | 1326 Hz | 1.27 | 7.1 dB   |
| Peaking | 4092 Hz | 1    | 6.8 dB   |
| Peaking | 1610 Hz | 5.08 | 3.2 dB   |
| Peaking | 2050 Hz | 2.8  | -4.6 dB  |
| Peaking | 2577 Hz | 3.15 | 4.0 dB   |
| Peaking | 6038 Hz | 2.63 | 6.2 dB   |
| Peaking | 6752 Hz | 1.11 | -4.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SENSO%20ActivBuds%20S-250/SENSO%20ActivBuds%20S-250.png)