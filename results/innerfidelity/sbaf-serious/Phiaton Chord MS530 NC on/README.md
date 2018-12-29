# Phiaton Chord MS530 NC on
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 6.0; 116 6.0; 128 6.0; 141 6.0; 155 6.0; 170 6.0; 187 6.0; 206 6.0; 227 6.0; 249 5.7; 274 5.5; 302 5.3; 332 4.8; 365 4.6; 402 4.1; 442 3.8; 486 3.2; 535 3.5; 588 2.5; 647 1.3; 712 0.8; 783 1.7; 861 1.1; 947 -0.1; 1042 -0.2; 1146 -0.4; 1261 0.6; 1387 0.3; 1526 2.9; 1678 2.5; 1846 2.1; 2031 4.2; 2234 5.6; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phiaton Chord MS530 NC on GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Chord MS530 NC on ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 37 Hz   |  0.16 | 6.0 dB  |
| Peaking | 277 Hz  |  0.79 | 3.1 dB  |
| Peaking | 2473 Hz |  2.09 | 5.0 dB  |
| Peaking | 3946 Hz |  1.79 | 4.8 dB  |
| Peaking | 5784 Hz |  3.12 | 4.7 dB  |
| Peaking | 527 Hz  |  6.73 | 1.2 dB  |
| Peaking | 1233 Hz |  1.21 | -1.6 dB |
| Peaking | 1581 Hz | 13.36 | 4.0 dB  |
| Peaking | 2343 Hz |  0.33 | 0.4 dB  |
| Peaking | 8375 Hz |  3.14 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20Chord%20MS530%20NC%20on/Phiaton%20Chord%20MS530%20NC%20on.png)