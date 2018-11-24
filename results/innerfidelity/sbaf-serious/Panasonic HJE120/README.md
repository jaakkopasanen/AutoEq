# Panasonic HJE120

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.4; 23 -7.4; 25 -7.5; 28 -7.6; 31 -7.6; 34 -7.3; 37 -7.1; 41 -7.1; 45 -7.4; 49 -7.6; 54 -7.8; 60 -7.7; 66 -7.8; 72 -8.1; 79 -8.3; 87 -8.4; 96 -8.4; 106 -8.5; 116 -8.2; 128 -8.2; 141 -8.3; 155 -7.9; 170 -7.7; 187 -7.4; 206 -7.0; 227 -6.5; 249 -6.1; 274 -5.5; 302 -5.0; 332 -4.4; 365 -3.8; 402 -3.2; 442 -2.5; 486 -2.1; 535 -1.6; 588 -0.8; 647 -0.3; 712 -0.1; 783 0.4; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -2.2; 1526 -3.7; 1678 -5.5; 1846 -7.3; 2031 -7.6; 2234 -5.5; 2457 -1.3; 2703 1.3; 2973 4.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.5; 4788 2.0; 5267 3.9; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic HJE120 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.2  | -7.2 dB |
| Peaking | 175 Hz  | 0.68 | -4.4 dB |
| Peaking | 1986 Hz | 2.53 | -9.7 dB |
| Peaking | 3448 Hz | 1.77 | 7.5 dB  |
| Peaking | 6077 Hz | 4.75 | 5.4 dB  |
| Peaking | 181 Hz  | 1.33 | 1.2 dB  |
| Peaking | 259 Hz  | 0.54 | -1.1 dB |
| Peaking | 792 Hz  | 1.34 | 1.8 dB  |
| Peaking | 1560 Hz | 4.57 | -1.1 dB |
| Peaking | 8339 Hz | 4.07 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20HJE120/Panasonic%20HJE120.png)