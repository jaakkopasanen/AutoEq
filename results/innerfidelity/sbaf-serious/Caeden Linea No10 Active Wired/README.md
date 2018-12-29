# Caeden Linea No10 Active Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.9; 23 -2.5; 25 -2.9; 28 -3.4; 31 -3.7; 34 -4.0; 37 -4.2; 41 -4.5; 45 -4.6; 49 -4.7; 54 -4.7; 60 -4.9; 66 -5.2; 72 -5.6; 79 -5.9; 87 -6.1; 96 -6.4; 106 -6.3; 116 -6.2; 128 -5.9; 141 -5.6; 155 -5.4; 170 -4.4; 187 -4.0; 206 -3.1; 227 -1.9; 249 -1.7; 274 -1.4; 302 -0.9; 332 -0.2; 365 0.5; 402 1.0; 442 1.6; 486 1.8; 535 2.0; 588 2.2; 647 2.0; 712 1.5; 783 1.2; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.7; 1387 -1.2; 1526 -1.7; 1678 -1.5; 1846 -0.7; 2031 -0.0; 2234 1.3; 2457 3.0; 2703 4.3; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.5; 4788 2.7; 5267 3.7; 5793 4.8; 6373 2.9; 7010 2.1; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Caeden Linea No10 Active Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Caeden Linea No10 Active Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.57 | -3.4 dB |
| Peaking | 118 Hz  | 0.8  | -5.3 dB |
| Peaking | 514 Hz  | 1.68 | 2.8 dB  |
| Peaking | 3477 Hz | 2.04 | 6.8 dB  |
| Peaking | 5820 Hz | 3.9  | 3.6 dB  |
| Peaking | 734 Hz  | 3.1  | 0.7 dB  |
| Peaking | 1605 Hz | 1.91 | -2.4 dB |
| Peaking | 2683 Hz | 4.34 | 1.8 dB  |
| Peaking | 7045 Hz | 3.78 | 0.9 dB  |
| Peaking | 7932 Hz | 2.59 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Caeden%20Linea%20No10%20Active%20Wired/Caeden%20Linea%20No10%20Active%20Wired.png)