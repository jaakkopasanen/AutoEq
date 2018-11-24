# Soul Jet Pro ANC On

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -2.0; 23 -3.7; 25 -5.2; 28 -7.0; 31 -8.1; 34 -8.4; 37 -8.0; 41 -7.4; 45 -6.9; 49 -6.7; 54 -6.4; 60 -6.2; 66 -6.2; 72 -6.1; 79 -6.1; 87 -6.3; 96 -6.5; 106 -6.6; 116 -6.8; 128 -7.4; 141 -7.9; 155 -8.3; 170 -8.4; 187 -8.7; 206 -9.0; 227 -9.1; 249 -9.3; 274 -9.3; 302 -9.6; 332 -9.8; 365 -9.7; 402 -9.5; 442 -8.4; 486 -5.0; 535 0.2; 588 3.2; 647 4.9; 712 4.2; 783 4.0; 861 2.5; 947 0.8; 1042 -0.5; 1146 -1.8; 1261 -3.3; 1387 -5.0; 1526 -8.2; 1678 -10.6; 1846 -13.3; 2031 -15.5; 2234 -15.3; 2457 -12.7; 2703 -9.7; 2973 -6.2; 3270 -4.0; 3597 -4.9; 3957 -7.4; 4353 -11.0; 4788 -7.9; 5267 -3.8; 5793 0.6; 6373 3.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Soul Jet Pro ANC On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Jet Pro ANC On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 64 Hz   | 0.15 | -6.2 dB  |
| Peaking | 420 Hz  | 0.83 | -14.0 dB |
| Peaking | 630 Hz  | 1.14 | 16.9 dB  |
| Peaking | 2065 Hz | 1.78 | -17.1 dB |
| Peaking | 4376 Hz | 6.04 | -9.7 dB  |
| Peaking | 34 Hz   | 3.77 | -2.4 dB  |
| Peaking | 2559 Hz | 4.86 | -1.6 dB  |
| Peaking | 3261 Hz | 6.65 | 2.0 dB   |
| Peaking | 4989 Hz | 5.87 | -2.7 dB  |
| Peaking | 6473 Hz | 4.28 | 5.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Jet%20Pro%20ANC%20On/Soul%20Jet%20Pro%20ANC%20On.png)