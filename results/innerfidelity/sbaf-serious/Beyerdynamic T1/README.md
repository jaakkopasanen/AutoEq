# Beyerdynamic T1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 21 0.0; 23 4.6; 25 4.1; 28 3.5; 31 3.1; 34 2.8; 37 2.5; 41 2.1; 45 1.8; 49 1.6; 54 1.6; 60 2.0; 66 1.4; 72 0.5; 79 -0.1; 87 -0.6; 96 -1.1; 106 -1.4; 116 -1.6; 128 -1.9; 141 -2.2; 155 -2.3; 170 -2.5; 187 -2.5; 206 -2.6; 227 -2.5; 249 -2.5; 274 -2.4; 302 -2.3; 332 -2.1; 365 -2.0; 402 -1.7; 442 -1.5; 486 -1.3; 535 -1.2; 588 -0.8; 647 -0.5; 712 -0.3; 783 -0.0; 861 -0.3; 947 -0.2; 1042 0.2; 1146 0.6; 1261 0.4; 1387 0.3; 1526 -0.2; 1678 -1.0; 1846 -1.5; 2031 -0.5; 2234 -0.0; 2457 -1.0; 2703 -0.7; 2973 -0.0; 3270 1.1; 3597 0.6; 3957 -0.1; 4353 -1.1; 4788 1.6; 5267 5.6; 5793 -2.1; 6373 -4.9; 7010 -0.6; 7711 -6.2; 8482 -10.3; 9330 -8.4; 10263 -2.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 16 Hz    |  0.6  | 5.7 dB   |
| Peaking | 62 Hz    |  3.44 | 1.6 dB   |
| Peaking | 194 Hz   |  0.56 | -2.8 dB  |
| Peaking | 5172 Hz  | 11.34 | 7.4 dB   |
| Peaking | 8617 Hz  |  3.61 | -11.3 dB |
| Peaking | 1818 Hz  |  3.22 | -3.6 dB  |
| Peaking | 2036 Hz  |  1.12 | 2.6 dB   |
| Peaking | 2534 Hz  |  3.81 | -2.4 dB  |
| Peaking | 6142 Hz  | 12.83 | -5.3 dB  |
| Peaking | 11204 Hz |  5.24 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1/Beyerdynamic%20T1.png)