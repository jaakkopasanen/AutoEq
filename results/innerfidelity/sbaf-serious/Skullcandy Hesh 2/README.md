# Skullcandy Hesh 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.0; 28 3.5; 31 3.2; 34 2.9; 37 2.7; 41 2.6; 45 2.5; 49 2.4; 54 2.4; 60 2.3; 66 2.2; 72 2.1; 79 2.0; 87 2.1; 96 2.2; 106 2.1; 116 2.3; 128 2.4; 141 1.8; 155 1.3; 170 1.7; 187 2.0; 206 1.9; 227 1.6; 249 1.8; 274 1.9; 302 1.9; 332 2.1; 365 2.4; 402 2.2; 442 1.8; 486 1.1; 535 0.5; 588 0.5; 647 0.1; 712 -0.2; 783 -0.0; 861 -0.1; 947 -0.0; 1042 0.2; 1146 0.5; 1261 0.9; 1387 1.1; 1526 1.1; 1678 1.8; 1846 2.6; 2031 3.9; 2234 5.2; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Hesh 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Hesh 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.4  | 5.8 dB  |
| Peaking | 107 Hz  | 0.88 | 1.7 dB  |
| Peaking | 242 Hz  | 1.77 | 1.1 dB  |
| Peaking | 377 Hz  | 3.3  | 2.0 dB  |
| Peaking | 3677 Hz | 0.83 | 6.9 dB  |
| Peaking | 1022 Hz | 1.12 | -0.8 dB |
| Peaking | 2372 Hz | 3.86 | 2.0 dB  |
| Peaking | 3676 Hz | 2.85 | -1.1 dB |
| Peaking | 6258 Hz | 2.36 | 5.4 dB  |
| Peaking | 7388 Hz | 1.5  | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Hesh%202/Skullcandy%20Hesh%202.png)