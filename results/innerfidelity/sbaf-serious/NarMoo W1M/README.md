# NarMoo W1M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.5; 28 -5.5; 31 -5.5; 34 -5.4; 37 -5.4; 41 -5.3; 45 -5.2; 49 -5.2; 54 -5.1; 60 -5.1; 66 -5.0; 72 -5.0; 79 -5.1; 87 -5.1; 96 -5.2; 106 -5.0; 116 -4.9; 128 -4.8; 141 -4.7; 155 -4.6; 170 -4.4; 187 -4.2; 206 -4.0; 227 -3.7; 249 -3.5; 274 -3.2; 302 -2.9; 332 -2.7; 365 -2.4; 402 -2.2; 442 -1.9; 486 -1.8; 535 -1.5; 588 -1.0; 647 -0.8; 712 -0.7; 783 -0.3; 861 -0.2; 947 -0.1; 1042 0.3; 1146 0.6; 1261 1.0; 1387 1.3; 1526 1.6; 1678 1.9; 1846 2.4; 2031 2.8; 2234 2.9; 2457 3.0; 2703 3.6; 2973 5.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 5.9; 4788 3.4; 5267 5.3; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo W1M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo W1M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.43 | -4.7 dB |
| Peaking | 129 Hz  |  0.36 | -4.3 dB |
| Peaking | 3641 Hz |  0.9  | 6.2 dB  |
| Peaking | 6165 Hz |  3.36 | 5.6 dB  |
| Peaking | 7049 Hz |  1.15 | -2.7 dB |
| Peaking | 2545 Hz |  3.32 | -2.2 dB |
| Peaking | 2547 Hz |  1.22 | 1.2 dB  |
| Peaking | 4888 Hz | 10.44 | -2.2 dB |
| Peaking | 5361 Hz |  7.84 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20W1M/NarMoo%20W1M.png)