# Sennheiser HD 800 sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.5; 28 1.1; 31 0.8; 34 0.5; 37 0.3; 41 0.1; 45 -0.0; 49 0.2; 54 0.4; 60 -0.4; 66 -0.1; 72 -0.8; 79 -1.8; 87 -2.3; 96 -2.7; 106 -3.1; 116 -3.3; 128 -3.6; 141 -3.8; 155 -4.0; 170 -4.0; 187 -4.2; 206 -4.2; 227 -4.2; 249 -4.1; 274 -4.1; 302 -3.9; 332 -3.6; 365 -3.4; 402 -3.2; 442 -2.9; 486 -2.8; 535 -2.4; 588 -2.2; 647 -1.8; 712 -1.5; 783 -1.2; 861 -1.0; 947 -0.1; 1042 0.2; 1146 1.2; 1261 1.2; 1387 1.0; 1526 0.6; 1678 1.1; 1846 1.1; 2031 1.3; 2234 0.4; 2457 1.5; 2703 1.8; 2973 0.0; 3270 0.4; 3597 0.1; 3957 -2.9; 4353 -3.2; 4788 -3.2; 5267 -4.4; 5793 -6.5; 6373 -9.5; 7010 -4.6; 7711 -4.4; 8482 -6.7; 9330 -9.3; 10263 -5.9; 11289 0.0; 12418 0.0; 13660 -1.1; 15026 -3.7; 16529 -3.7; 18182 -5.0; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.22 | 2.0 dB  |
| Peaking | 201 Hz   | 0.35 | -4.7 dB |
| Peaking | 2532 Hz  | 0.49 | 2.9 dB  |
| Peaking | 6639 Hz  | 0.88 | -8.2 dB |
| Peaking | 19099 Hz | 1.2  | -5.8 dB |
| Peaking | 6251 Hz  | 9.35 | -5.5 dB |
| Peaking | 7286 Hz  | 2.84 | 3.9 dB  |
| Peaking | 9590 Hz  | 3.22 | -9.3 dB |
| Peaking | 11244 Hz | 1.83 | 6.1 dB  |
| Peaking | 15097 Hz | 3.02 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20sample%202/Sennheiser%20HD%20800%20sample%202.png)