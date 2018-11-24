# Lear LUF-4F

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.8; 28 0.5; 31 0.2; 34 -0.0; 37 -0.2; 41 -0.5; 45 -0.8; 49 -1.0; 54 -1.3; 60 -1.7; 66 -2.0; 72 -2.3; 79 -2.6; 87 -2.9; 96 -3.2; 106 -3.3; 116 -3.2; 128 -3.2; 141 -2.9; 155 -2.6; 170 -2.1; 187 -1.4; 206 -0.8; 227 -0.0; 249 0.5; 274 1.0; 302 1.4; 332 1.6; 365 1.8; 402 1.8; 442 1.9; 486 1.8; 535 1.8; 588 2.0; 647 1.9; 712 1.6; 783 1.6; 861 1.1; 947 0.5; 1042 -0.3; 1146 -1.1; 1261 -2.0; 1387 -3.3; 1526 -4.8; 1678 -5.8; 1846 -6.4; 2031 -6.6; 2234 -6.5; 2457 -5.3; 2703 -3.4; 2973 -0.7; 3270 0.3; 3597 -0.3; 3957 1.0; 4353 5.4; 4788 6.0; 5267 1.0; 5793 0.3; 6373 1.9; 7010 1.4; 7711 -2.4; 8482 -3.7; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF-4F GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF-4F ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 125 Hz  |  0.72 | -5.4 dB |
| Peaking | 361 Hz  |  0.28 | 3.2 dB  |
| Peaking | 1901 Hz |  1.38 | -8.2 dB |
| Peaking | 4581 Hz |  4.02 | 7.2 dB  |
| Peaking | 8269 Hz |  8.12 | -4.7 dB |
| Peaking | 20 Hz   |  1.64 | 1.4 dB  |
| Peaking | 2429 Hz |  6.46 | -1.3 dB |
| Peaking | 3104 Hz |  8.01 | 2.1 dB  |
| Peaking | 5505 Hz | 11.64 | -2.3 dB |
| Peaking | 6616 Hz |  7.28 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF-4F/Lear%20LUF-4F.png)