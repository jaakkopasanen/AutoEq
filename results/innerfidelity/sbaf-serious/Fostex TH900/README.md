# Fostex TH900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -3.6; 23 -3.9; 25 -4.1; 28 -4.3; 31 -4.4; 34 -4.4; 37 -4.5; 41 -4.4; 45 -4.3; 49 -4.1; 54 -4.0; 60 -4.3; 66 -4.6; 72 -4.8; 79 -5.0; 87 -5.3; 96 -5.6; 106 -5.6; 116 -5.6; 128 -5.7; 141 -5.6; 155 -5.3; 170 -4.9; 187 -4.8; 206 -4.5; 227 -4.0; 249 -3.6; 274 -3.0; 302 -2.5; 332 -1.8; 365 -0.8; 402 0.2; 442 1.6; 486 2.6; 535 3.9; 588 4.1; 647 2.9; 712 1.7; 783 1.7; 861 0.5; 947 0.1; 1042 0.0; 1146 0.1; 1261 0.4; 1387 0.2; 1526 0.0; 1678 -0.2; 1846 0.1; 2031 1.9; 2234 3.2; 2457 3.0; 2703 3.0; 2973 1.8; 3270 1.6; 3597 1.8; 3957 2.8; 4353 0.5; 4788 -0.6; 5267 -0.5; 5793 -2.2; 6373 -2.4; 7010 -2.0; 7711 -1.3; 8482 -0.1; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -2.3; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.86 | -3.3 dB |
| Peaking | 130 Hz  | 0.45 | -5.5 dB |
| Peaking | 547 Hz  | 2    | 5.5 dB  |
| Peaking | 2700 Hz | 1.65 | 3.1 dB  |
| Peaking | 6363 Hz | 3.02 | -3.0 dB |
| Peaking | 1856 Hz | 3.01 | -1.9 dB |
| Peaking | 2144 Hz | 3.77 | 2.4 dB  |
| Peaking | 3502 Hz | 1.75 | -1.3 dB |
| Peaking | 3877 Hz | 5.88 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900/Fostex%20TH900.png)