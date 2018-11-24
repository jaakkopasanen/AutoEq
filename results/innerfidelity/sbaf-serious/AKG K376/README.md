# AKG K376

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 -13.1; 23 -13.0; 25 -12.9; 28 -12.7; 31 -12.6; 34 -12.4; 37 -12.2; 41 -12.0; 45 -11.9; 49 -11.7; 54 -11.5; 60 -11.3; 66 -11.2; 72 -11.1; 79 -10.9; 87 -10.8; 96 -10.7; 106 -10.4; 116 -10.0; 128 -9.7; 141 -9.4; 155 -9.0; 170 -8.5; 187 -8.0; 206 -7.5; 227 -6.8; 249 -6.3; 274 -5.6; 302 -5.0; 332 -4.3; 365 -3.6; 402 -3.0; 442 -2.3; 486 -1.8; 535 -1.2; 588 -0.5; 647 0.2; 712 0.3; 783 0.8; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.9; 1387 -1.6; 1526 -2.4; 1678 -3.2; 1846 -3.6; 2031 -4.1; 2234 -5.0; 2457 -5.6; 2703 -5.5; 2973 -2.5; 3270 0.9; 3597 2.4; 3957 1.3; 4353 -1.2; 4788 -4.0; 5267 -5.9; 5793 -4.5; 6373 -0.1; 7010 2.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K376 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K376 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 22 Hz   | 0.19 | -12.7 dB |
| Peaking | 165 Hz  | 0.73 | -4.3 dB  |
| Peaking | 2526 Hz | 1.75 | -7.2 dB  |
| Peaking | 3493 Hz | 2.7  | 5.7 dB   |
| Peaking | 5242 Hz | 4.91 | -6.8 dB  |
| Peaking | 335 Hz  | 2.07 | -0.8 dB  |
| Peaking | 781 Hz  | 1.63 | 1.9 dB   |
| Peaking | 1626 Hz | 3.82 | -1.3 dB  |
| Peaking | 5829 Hz | 7.25 | -1.8 dB  |
| Peaking | 6868 Hz | 6.11 | 3.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K376/AKG%20K376.png)