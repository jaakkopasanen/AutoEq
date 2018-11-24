# Monster Jamz

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.7; 28 4.0; 31 3.4; 34 2.9; 37 2.4; 41 1.9; 45 1.4; 49 0.9; 54 0.3; 60 -0.3; 66 -1.0; 72 -1.5; 79 -2.1; 87 -2.7; 96 -3.2; 106 -3.7; 116 -4.2; 128 -4.7; 141 -5.1; 155 -5.6; 170 -5.8; 187 -6.1; 206 -6.2; 227 -6.0; 249 -5.8; 274 -5.9; 302 -5.9; 332 -5.5; 365 -5.0; 402 -4.5; 442 -4.0; 486 -3.4; 535 -2.7; 588 -2.1; 647 -1.4; 712 -0.8; 783 -0.3; 861 -0.1; 947 -0.1; 1042 0.0; 1146 0.0; 1261 -0.1; 1387 -0.1; 1526 -0.4; 1678 -0.2; 1846 0.1; 2031 0.5; 2234 1.4; 2457 2.7; 2703 4.1; 2973 5.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.0; 4788 5.1; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.59 | 6.5 dB  |
| Peaking | 163 Hz  | 0.63 | -5.3 dB |
| Peaking | 338 Hz  | 1.18 | -3.0 dB |
| Peaking | 3417 Hz | 1.84 | 6.2 dB  |
| Peaking | 5676 Hz | 2.85 | 5.5 dB  |
| Peaking | 886 Hz  | 2.59 | 0.8 dB  |
| Peaking | 1775 Hz | 2.03 | -0.9 dB |
| Peaking | 2730 Hz | 5.05 | 0.9 dB  |
| Peaking | 6593 Hz | 7.51 | 2.2 dB  |
| Peaking | 7815 Hz | 2.28 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)