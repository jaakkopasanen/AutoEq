# JAYS j-Jays
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.7; 23 -4.8; 25 -4.8; 28 -4.9; 31 -4.9; 34 -5.0; 37 -5.0; 41 -5.1; 45 -5.2; 49 -5.2; 54 -5.4; 60 -5.7; 66 -6.0; 72 -6.1; 79 -6.4; 87 -6.5; 96 -6.7; 106 -6.8; 116 -6.8; 128 -6.9; 141 -7.1; 155 -7.0; 170 -6.8; 187 -6.6; 206 -6.2; 227 -5.7; 249 -5.3; 274 -5.5; 302 -4.9; 332 -4.2; 365 -3.4; 402 -2.7; 442 -2.3; 486 -1.6; 535 -1.0; 588 -0.4; 647 0.1; 712 0.4; 783 0.5; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -1.0; 1387 -1.7; 1526 -3.5; 1678 -4.2; 1846 -3.8; 2031 -2.8; 2234 -1.2; 2457 1.0; 2703 3.4; 2973 5.8; 3270 6.0; 3597 6.0; 3957 5.4; 4353 0.7; 4788 -4.1; 5267 0.3; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JAYS j-Jays GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS j-Jays ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.23 | -4.6 dB |
| Peaking | 152 Hz   | 0.72 | -4.3 dB |
| Peaking | 292 Hz   | 1.94 | -2.0 dB |
| Peaking | 3379 Hz  | 3.41 | 7.2 dB  |
| Peaking | 22544 Hz | 2.33 | 3.6 dB  |
| Peaking | 798 Hz   | 1.85 | 1.5 dB  |
| Peaking | 1758 Hz  | 2.2  | -4.8 dB |
| Peaking | 2797 Hz  | 5.08 | 2.7 dB  |
| Peaking | 4851 Hz  | 7.7  | -7.3 dB |
| Peaking | 5987 Hz  | 3.92 | 6.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/JAYS%20j-Jays/JAYS%20j-Jays.png)