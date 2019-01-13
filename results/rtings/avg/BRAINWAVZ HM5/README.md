# BRAINWAVZ HM5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.6; 28 3.4; 31 3.3; 34 3.3; 37 3.3; 41 3.3; 45 3.3; 49 3.1; 54 2.9; 60 2.5; 66 2.1; 72 1.7; 79 1.3; 87 0.7; 96 0.0; 106 -0.6; 116 -1.1; 128 -1.5; 141 -1.8; 155 -1.9; 170 -1.9; 187 -1.8; 206 -1.5; 227 -1.0; 249 -0.2; 274 1.0; 302 2.5; 332 3.9; 365 4.2; 402 3.3; 442 2.3; 486 1.2; 535 0.5; 588 -0.1; 647 -0.4; 712 -0.3; 783 -0.0; 861 0.2; 947 0.0; 1042 -0.0; 1146 0.1; 1261 -0.2; 1387 -0.5; 1526 -0.9; 1678 -1.6; 1846 -2.5; 2031 -2.6; 2234 -2.0; 2457 -1.3; 2703 -1.1; 2973 -0.4; 3270 -0.4; 3597 -4.0; 3957 -3.7; 4353 -3.7; 4788 -3.4; 5267 -1.9; 5793 -2.3; 6373 -1.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -2.9; 15026 -2.3; 16529 -0.0; 18182 0.0; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BRAINWAVZ HM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BRAINWAVZ HM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 17 Hz    |  0.34 | 3.5 dB  |
| Peaking | 64 Hz    |  0.77 | 2.8 dB  |
| Peaking | 201 Hz   |  0.37 | -4.2 dB |
| Peaking | 355 Hz   |  1.49 | 7.4 dB  |
| Peaking | 4185 Hz  |  1.97 | -4.0 dB |
| Peaking | 1054 Hz  |  1.93 | 0.8 dB  |
| Peaking | 1948 Hz  |  2.85 | -2.3 dB |
| Peaking | 3113 Hz  | 10.35 | 2.4 dB  |
| Peaking | 6935 Hz  | 11.7  | 3.9 dB  |
| Peaking | 14152 Hz |  4.22 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/BRAINWAVZ%20HM5/BRAINWAVZ%20HM5.png)