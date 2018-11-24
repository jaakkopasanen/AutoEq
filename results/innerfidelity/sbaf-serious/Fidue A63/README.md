# Fidue A63

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -0.1; 23 -0.6; 25 -1.0; 28 -1.7; 31 -2.4; 34 -2.9; 37 -3.3; 41 -3.8; 45 -4.3; 49 -4.6; 54 -5.1; 60 -5.5; 66 -6.0; 72 -6.4; 79 -6.9; 87 -7.2; 96 -7.7; 106 -7.9; 116 -8.1; 128 -8.2; 141 -8.3; 155 -8.4; 170 -8.2; 187 -8.0; 206 -7.8; 227 -7.4; 249 -7.1; 274 -6.6; 302 -6.2; 332 -5.7; 365 -5.1; 402 -4.5; 442 -3.8; 486 -3.4; 535 -2.7; 588 -1.9; 647 -1.4; 712 -1.2; 783 -0.8; 861 -0.6; 947 0.1; 1042 -0.1; 1146 -0.7; 1261 -1.5; 1387 -2.3; 1526 -2.9; 1678 -3.4; 1846 -3.4; 2031 -3.1; 2234 -2.9; 2457 -2.1; 2703 -1.1; 2973 0.8; 3270 2.8; 3597 4.1; 3957 3.9; 4353 2.6; 4788 2.3; 5267 3.2; 5793 3.2; 6373 3.4; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A63 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A63 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 109 Hz  | 0.48 | -7.3 dB |
| Peaking | 262 Hz  | 0.9  | -3.4 dB |
| Peaking | 1979 Hz | 1.67 | -3.9 dB |
| Peaking | 3653 Hz | 2.85 | 4.8 dB  |
| Peaking | 5955 Hz | 2.75 | 3.5 dB  |
| Peaking | 16 Hz   | 1.86 | 1.1 dB  |
| Peaking | 461 Hz  | 3.16 | -0.6 dB |
| Peaking | 992 Hz  | 1.76 | 1.3 dB  |
| Peaking | 1431 Hz | 3.39 | -1.1 dB |
| Peaking | 8314 Hz | 5.09 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A63/Fidue%20A63.png)