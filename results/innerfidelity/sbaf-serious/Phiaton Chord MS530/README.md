# Phiaton Chord MS530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 5.3; 28 5.0; 31 4.7; 34 4.5; 37 4.3; 41 4.1; 45 3.9; 49 3.7; 54 3.5; 60 3.1; 66 2.8; 72 2.6; 79 2.3; 87 2.4; 96 2.4; 106 1.7; 116 1.5; 128 1.4; 141 1.1; 155 1.1; 170 1.7; 187 1.6; 206 2.1; 227 2.6; 249 3.1; 274 3.6; 302 4.0; 332 4.2; 365 4.3; 402 3.9; 442 3.9; 486 3.9; 535 3.5; 588 3.3; 647 2.7; 712 2.1; 783 1.9; 861 1.1; 947 0.6; 1042 -0.4; 1146 -1.1; 1261 -1.2; 1387 -1.9; 1526 0.3; 1678 -1.3; 1846 -1.7; 2031 -0.3; 2234 0.9; 2457 2.8; 2703 4.2; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.61 | 5.4 dB  |
| Peaking | 60 Hz   | 1.03 | 1.5 dB  |
| Peaking | 412 Hz  | 0.75 | 4.4 dB  |
| Peaking | 1627 Hz | 0.99 | -3.8 dB |
| Peaking | 3820 Hz | 0.91 | 7.6 dB  |
| Peaking | 1138 Hz | 6.32 | -0.5 dB |
| Peaking | 2967 Hz | 4.58 | 1.3 dB  |
| Peaking | 3864 Hz | 2.85 | -1.1 dB |
| Peaking | 6268 Hz | 2.45 | 5.4 dB  |
| Peaking | 7360 Hz | 1.51 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530/Phiaton%20Chord%20MS530.png)