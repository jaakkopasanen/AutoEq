# Pioneer HDJ-1000 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.2; 87 3.4; 96 2.1; 106 1.4; 116 0.9; 128 0.6; 141 0.6; 155 0.7; 170 0.9; 187 1.1; 206 1.1; 227 1.1; 249 1.3; 274 1.7; 302 1.8; 332 1.9; 365 2.1; 402 2.3; 442 2.7; 486 2.2; 535 2.0; 588 3.2; 647 3.0; 712 2.4; 783 1.6; 861 0.9; 947 0.2; 1042 -0.1; 1146 -0.7; 1261 -1.6; 1387 -2.7; 1526 -3.4; 1678 -3.0; 1846 -1.5; 2031 0.5; 2234 2.6; 2457 4.6; 2703 5.7; 2973 6.0; 3270 6.0; 3597 6.0; 3957 4.2; 4353 4.3; 4788 6.0; 5267 6.0; 5793 5.3; 6373 3.1; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-1000 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.6  | 6.9 dB  |
| Peaking | 563 Hz  | 0.97 | 2.9 dB  |
| Peaking | 1594 Hz | 1.64 | -5.7 dB |
| Peaking | 2886 Hz | 1.33 | 7.0 dB  |
| Peaking | 5326 Hz | 2.85 | 4.9 dB  |
| Peaking | 39 Hz   | 2.85 | -1.1 dB |
| Peaking | 72 Hz   | 2.96 | 2.4 dB  |
| Peaking | 119 Hz  | 2.02 | -1.5 dB |
| Peaking | 6812 Hz | 9.64 | 2.2 dB  |
| Peaking | 7996 Hz | 2.16 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Pioneer%20HDJ-1000%20Gold/Pioneer%20HDJ-1000%20Gold.png)