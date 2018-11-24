# Brainwavz S0

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 -6.8; 23 -7.0; 25 -7.1; 28 -7.3; 31 -7.5; 34 -7.6; 37 -7.7; 41 -7.9; 45 -8.0; 49 -8.2; 54 -8.4; 60 -8.6; 66 -8.9; 72 -9.1; 79 -9.4; 87 -9.6; 96 -9.9; 106 -10.0; 116 -10.0; 128 -10.1; 141 -10.1; 155 -10.0; 170 -9.8; 187 -9.6; 206 -9.3; 227 -8.8; 249 -8.5; 274 -8.0; 302 -7.4; 332 -6.9; 365 -6.2; 402 -5.5; 442 -4.8; 486 -4.3; 535 -3.5; 588 -2.6; 647 -2.0; 712 -1.6; 783 -0.9; 861 -0.5; 947 -0.2; 1042 0.3; 1146 0.1; 1261 0.5; 1387 0.9; 1526 0.6; 1678 -1.6; 1846 -2.7; 2031 -2.3; 2234 -1.8; 2457 -0.9; 2703 -0.2; 2973 0.9; 3270 1.4; 3597 1.1; 3957 -0.2; 4353 -3.6; 4788 -6.7; 5267 -8.4; 5793 -3.4; 6373 1.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.3  | -6.6 dB |
| Peaking | 117 Hz  | 0.7  | -5.5 dB |
| Peaking | 227 Hz  | 0.99 | -4.6 dB |
| Peaking | 397 Hz  | 1.55 | -2.5 dB |
| Peaking | 5085 Hz | 5.8  | -9.5 dB |
| Peaking | 1497 Hz | 1.88 | 3.9 dB  |
| Peaking | 1823 Hz | 2.08 | -5.0 dB |
| Peaking | 3493 Hz | 2.47 | 3.7 dB  |
| Peaking | 4344 Hz | 1.5  | -2.3 dB |
| Peaking | 6716 Hz | 5.92 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S0/Brainwavz%20S0.png)