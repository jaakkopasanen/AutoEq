# Plugged Crown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.4; 28 0.1; 31 -0.2; 34 -0.5; 37 -0.8; 41 -1.0; 45 -1.3; 49 -1.6; 54 -1.8; 60 -2.2; 66 -2.5; 72 -2.8; 79 -2.9; 87 -2.8; 96 -3.1; 106 -4.2; 116 -5.2; 128 -6.0; 141 -6.3; 155 -6.4; 170 -6.2; 187 -7.1; 206 -7.2; 227 -6.8; 249 -7.0; 274 -7.1; 302 -6.8; 332 -6.2; 365 -5.3; 402 -4.2; 442 -2.4; 486 -1.7; 535 -0.2; 588 1.8; 647 3.1; 712 3.4; 783 2.8; 861 1.5; 947 0.4; 1042 -0.0; 1146 -0.7; 1261 -1.0; 1387 -1.1; 1526 -1.0; 1678 -1.7; 1846 -2.1; 2031 -1.5; 2234 -0.4; 2457 1.0; 2703 2.0; 2973 3.6; 3270 4.8; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plugged Crown GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plugged Crown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 132 Hz  | 3.27 | -1.0 dB |
| Peaking | 256 Hz  | 0.46 | -7.6 dB |
| Peaking | 661 Hz  | 1.61 | 7.2 dB  |
| Peaking | 1857 Hz | 1.77 | -3.1 dB |
| Peaking | 4294 Hz | 1.12 | 7.1 dB  |
| Peaking | 19 Hz   | 1.83 | 1.4 dB  |
| Peaking | 3441 Hz | 3.5  | 1.0 dB  |
| Peaking | 4263 Hz | 3.32 | -1.1 dB |
| Peaking | 6309 Hz | 2.94 | 4.6 dB  |
| Peaking | 7424 Hz | 1.59 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Plugged%20Crown/Plugged%20Crown.png)