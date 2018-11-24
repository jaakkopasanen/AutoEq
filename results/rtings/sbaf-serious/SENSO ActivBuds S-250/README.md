# SENSO ActivBuds S-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.7; 25 0.3; 28 -0.3; 31 -0.8; 34 -1.2; 37 -1.6; 41 -2.1; 45 -2.5; 49 -3.0; 54 -3.6; 60 -4.4; 66 -5.1; 72 -5.6; 79 -6.3; 87 -7.1; 96 -8.1; 106 -9.2; 116 -10.3; 128 -11.4; 141 -12.4; 155 -13.2; 170 -13.9; 187 -14.6; 206 -15.1; 227 -15.3; 249 -15.2; 274 -14.9; 302 -14.5; 332 -13.9; 365 -13.2; 402 -12.4; 442 -11.5; 486 -10.2; 535 -8.8; 588 -7.4; 647 -5.6; 712 -4.0; 783 -2.7; 861 -1.5; 947 -0.5; 1042 0.5; 1146 1.8; 1261 3.5; 1387 5.3; 1526 6.0; 1678 5.1; 1846 2.3; 2031 1.0; 2234 2.7; 2457 5.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SENSO ActivBuds S-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SENSO ActivBuds S-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 1.44 | 1.9 dB   |
| Peaking | 183 Hz  | 0.56 | -12.2 dB |
| Peaking | 366 Hz  | 0.91 | -6.8 dB  |
| Peaking | 1403 Hz | 2.26 | 6.0 dB   |
| Peaking | 3950 Hz | 0.93 | 6.9 dB   |
| Peaking | 2054 Hz | 4.24 | -5.3 dB  |
| Peaking | 2404 Hz | 1.51 | 3.7 dB   |
| Peaking | 3666 Hz | 1.77 | -1.9 dB  |
| Peaking | 6276 Hz | 2.52 | 5.1 dB   |
| Peaking | 7420 Hz | 1.54 | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SENSO%20ActivBuds%20S-250/SENSO%20ActivBuds%20S-250.png)