# Earsonics Velvet Pot CW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.3; 23 -3.6; 25 -3.9; 28 -4.1; 31 -4.3; 34 -4.4; 37 -4.4; 41 -4.6; 45 -4.7; 49 -4.8; 54 -4.8; 60 -4.9; 66 -5.0; 72 -5.0; 79 -5.0; 87 -5.0; 96 -4.9; 106 -4.5; 116 -4.0; 128 -3.6; 141 -2.9; 155 -2.1; 170 -1.2; 187 -0.1; 206 1.1; 227 2.3; 249 3.2; 274 3.8; 302 4.1; 332 3.9; 365 3.6; 402 3.1; 442 2.7; 486 2.1; 535 1.8; 588 1.8; 647 1.6; 712 1.2; 783 1.2; 861 0.8; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.4; 1526 -1.7; 1678 -1.6; 1846 -0.6; 2031 1.5; 2234 3.3; 2457 4.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.9; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Earsonics Velvet Pot CW GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.4  | -3.3 dB |
| Peaking | 121 Hz  | 0.52 | -4.7 dB |
| Peaking | 279 Hz  | 0.85 | 6.5 dB  |
| Peaking | 1580 Hz | 1.83 | -4.6 dB |
| Peaking | 3522 Hz | 0.78 | 7.2 dB  |
| Peaking | 1871 Hz | 8.14 | -0.7 dB |
| Peaking | 2646 Hz | 3    | 1.2 dB  |
| Peaking | 3458 Hz | 2.54 | -1.1 dB |
| Peaking | 6154 Hz | 2.47 | 5.3 dB  |
| Peaking | 7328 Hz | 1.44 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CW/Earsonics%20Velvet%20Pot%20CW.png)