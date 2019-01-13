# Sonoma Model One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 1.4; 25 1.3; 28 1.3; 31 1.3; 34 1.4; 37 1.4; 41 1.4; 45 1.6; 49 1.7; 54 1.9; 60 2.1; 66 1.5; 72 0.1; 79 -0.5; 87 -0.1; 96 0.2; 106 0.4; 116 0.3; 128 0.5; 141 0.6; 155 0.6; 170 0.6; 187 0.5; 206 0.5; 227 0.6; 249 0.6; 274 0.6; 302 0.6; 332 0.5; 365 0.5; 402 0.6; 442 0.5; 486 -0.1; 535 0.1; 588 0.6; 647 -0.3; 712 -1.2; 783 -0.8; 861 -0.8; 947 -0.2; 1042 0.3; 1146 -1.2; 1261 -2.4; 1387 -2.3; 1526 -3.5; 1678 -2.1; 1846 -1.3; 2031 -0.7; 2234 -1.5; 2457 -0.3; 2703 -1.9; 2973 -0.7; 3270 -1.6; 3597 -0.8; 3957 0.2; 4353 0.0; 4788 0.1; 5267 -1.1; 5793 4.8; 6373 1.7; 7010 0.9; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -1.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sonoma Model One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sonoma Model One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 35 Hz   |  0.57 | 1.6 dB  |
| Peaking | 1423 Hz |  2.48 | -1.8 dB |
| Peaking | 1538 Hz |  4.54 | -1.5 dB |
| Peaking | 2914 Hz |  2.09 | -1.2 dB |
| Peaking | 5953 Hz | 11.04 | 6.3 dB  |
| Peaking | 64 Hz   |  3.45 | 1.9 dB  |
| Peaking | 76 Hz   |  2.59 | -2.0 dB |
| Peaking | 373 Hz  |  0.34 | 0.5 dB  |
| Peaking | 730 Hz  |  4.49 | -1.5 dB |
| Peaking | 1487 Hz |  1.43 | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sonoma%20Model%20One/Sonoma%20Model%20One.png)