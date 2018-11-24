# Nixon RPM

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.6; 31 4.7; 34 3.7; 37 2.9; 41 1.9; 45 1.2; 49 0.6; 54 0.1; 60 -0.1; 66 -0.7; 72 -1.3; 79 -1.6; 87 -1.9; 96 -2.2; 106 -2.0; 116 -2.0; 128 -2.3; 141 -2.3; 155 -2.3; 170 -2.1; 187 -2.1; 206 -2.1; 227 -1.8; 249 -1.8; 274 -1.5; 302 -1.5; 332 -2.6; 365 -2.0; 402 -1.4; 442 -1.1; 486 -0.5; 535 0.3; 588 0.8; 647 0.8; 712 0.4; 783 0.3; 861 -0.2; 947 -0.2; 1042 0.3; 1146 0.7; 1261 0.5; 1387 1.0; 1526 1.8; 1678 2.6; 1846 4.2; 2031 5.8; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 3.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Nixon RPM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nixon RPM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.92 | 7.7 dB  |
| Peaking | 230 Hz  | 0.09 | -2.5 dB |
| Peaking | 609 Hz  | 1.87 | 2.7 dB  |
| Peaking | 2705 Hz | 0.83 | 7.7 dB  |
| Peaking | 5754 Hz | 3.55 | 4.4 dB  |
| Peaking | 271 Hz  | 5.5  | 0.6 dB  |
| Peaking | 2067 Hz | 3.57 | 2.6 dB  |
| Peaking | 2207 Hz | 1.43 | -1.7 dB |
| Peaking | 4074 Hz | 5.25 | 1.6 dB  |
| Peaking | 8568 Hz | 2.95 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nixon%20RPM/Nixon%20RPM.png)