# House of Marley Legend

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.3; 25 1.1; 28 0.9; 31 0.7; 34 0.5; 37 0.4; 41 0.1; 45 -0.1; 49 -0.2; 54 -0.6; 60 -0.9; 66 -1.2; 72 -1.6; 79 -2.0; 87 -2.4; 96 -2.9; 106 -3.1; 116 -3.2; 128 -3.6; 141 -3.9; 155 -4.0; 170 -4.1; 187 -4.1; 206 -4.1; 227 -4.0; 249 -3.9; 274 -3.7; 302 -3.5; 332 -3.3; 365 -2.9; 402 -2.6; 442 -2.1; 486 -1.8; 535 -1.4; 588 -0.6; 647 -0.2; 712 0.1; 783 0.4; 861 0.2; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.3; 1526 -1.8; 1678 -2.3; 1846 -2.2; 2031 -1.9; 2234 -1.2; 2457 0.5; 2703 1.6; 2973 4.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.4; 5793 5.5; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`House of Marley Legend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `House of Marley Legend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.61 | 1.8 dB  |
| Peaking | 147 Hz  | 0.71 | -3.7 dB |
| Peaking | 305 Hz  | 1.35 | -2.1 dB |
| Peaking | 1951 Hz | 1.8  | -4.3 dB |
| Peaking | 4070 Hz | 1.04 | 7.2 dB  |
| Peaking | 807 Hz  | 2.09 | 1.1 dB  |
| Peaking | 2390 Hz | 0.13 | -0.3 dB |
| Peaking | 3194 Hz | 8.9  | 1.8 dB  |
| Peaking | 6332 Hz | 3.39 | 5.1 dB  |
| Peaking | 7215 Hz | 1.6  | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/House%20of%20Marley%20Legend/House%20of%20Marley%20Legend.png)