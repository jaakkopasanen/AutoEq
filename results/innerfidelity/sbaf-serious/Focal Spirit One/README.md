# Focal Spirit One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.5; 28 -4.5; 31 -4.6; 34 -4.6; 37 -4.5; 41 -4.4; 45 -4.3; 49 -4.2; 54 -4.2; 60 -4.3; 66 -4.2; 72 -3.9; 79 -3.4; 87 -4.1; 96 -5.9; 106 -6.5; 116 -6.4; 128 -6.1; 141 -6.2; 155 -6.0; 170 -5.6; 187 -5.3; 206 -4.7; 227 -3.8; 249 -3.1; 274 -2.2; 302 -1.4; 332 -1.4; 365 -1.3; 402 -2.1; 442 -2.1; 486 -2.2; 535 -2.2; 588 -1.7; 647 -1.8; 712 -1.8; 783 -1.3; 861 -1.1; 947 -0.5; 1042 -0.2; 1146 -0.5; 1261 -0.2; 1387 -0.4; 1526 -0.6; 1678 -0.5; 1846 0.2; 2031 1.0; 2234 2.0; 2457 3.3; 2703 4.2; 2973 5.8; 3270 5.5; 3597 6.0; 3957 3.0; 4353 0.6; 4788 0.0; 5267 0.1; 5793 3.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Spirit One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Spirit One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.52 | -4.4 dB |
| Peaking | 137 Hz  | 0.95 | -5.7 dB |
| Peaking | 1602 Hz | 0.15 | -1.2 dB |
| Peaking | 3104 Hz | 1.92 | 7.3 dB  |
| Peaking | 6359 Hz | 5.77 | 6.4 dB  |
| Peaking | 319 Hz  | 2.91 | 1.6 dB  |
| Peaking | 639 Hz  | 0.5  | -1.0 dB |
| Peaking | 1016 Hz | 1.85 | 1.5 dB  |
| Peaking | 4648 Hz | 3.32 | -3.9 dB |
| Peaking | 4652 Hz | 1.62 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Focal%20Spirit%20One/Focal%20Spirit%20One.png)