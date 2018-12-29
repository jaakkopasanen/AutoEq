# Musical Fidelity MF100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 1.3; 25 0.7; 28 0.0; 31 -0.5; 34 -1.0; 37 -1.3; 41 -1.5; 45 -1.6; 49 -1.6; 54 -1.5; 60 -1.5; 66 -1.4; 72 -1.2; 79 -0.8; 87 0.1; 96 -0.2; 106 -0.3; 116 -0.1; 128 0.1; 141 0.6; 155 0.5; 170 1.0; 187 1.1; 206 1.3; 227 1.7; 249 2.2; 274 2.8; 302 2.7; 332 3.0; 365 2.8; 402 2.6; 442 2.4; 486 2.3; 535 2.4; 588 2.8; 647 3.0; 712 3.2; 783 2.8; 861 1.3; 947 0.3; 1042 0.1; 1146 0.3; 1261 -0.2; 1387 -0.1; 1526 0.1; 1678 -0.3; 1846 -0.7; 2031 -1.1; 2234 -1.4; 2457 -1.2; 2703 -1.2; 2973 -1.1; 3270 -1.1; 3597 -0.8; 3957 0.2; 4353 -1.2; 4788 -2.4; 5267 -0.5; 5793 -0.2; 6373 0.1; 7010 -2.8; 7711 -2.4; 8482 -3.9; 9330 -4.0; 10263 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Musical Fidelity MF100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Musical Fidelity MF100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 18 Hz    |  1.5  | 3.1 dB  |
| Peaking | 49 Hz    |  0.99 | -2.0 dB |
| Peaking | 322 Hz   |  1.11 | 3.0 dB  |
| Peaking | 683 Hz   |  3.07 | 2.8 dB  |
| Peaking | 8529 Hz  |  2.88 | -4.2 dB |
| Peaking | 25 Hz    |  1.38 | -0.4 dB |
| Peaking | 530 Hz   |  4.55 | 0.4 dB  |
| Peaking | 2378 Hz  |  1.7  | -1.4 dB |
| Peaking | 4721 Hz  | 10.4  | -2.4 dB |
| Peaking | 10662 Hz |  5.72 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Musical%20Fidelity%20MF100/Musical%20Fidelity%20MF100.png)