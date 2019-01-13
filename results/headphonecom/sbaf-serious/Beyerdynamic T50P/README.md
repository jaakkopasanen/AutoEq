# Beyerdynamic T50p
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.5; 34 4.9; 37 4.2; 41 3.5; 45 2.9; 49 2.3; 54 1.4; 60 0.7; 66 1.7; 72 1.6; 79 0.4; 87 -0.3; 96 -0.3; 106 -0.3; 116 -0.2; 128 0.3; 141 1.0; 155 3.1; 170 3.8; 187 1.4; 206 -0.9; 227 -1.5; 249 -2.3; 274 -4.0; 302 -5.6; 332 -5.3; 365 -4.9; 402 -4.4; 442 -4.3; 486 -3.8; 535 -3.4; 588 -3.0; 647 -2.5; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.3; 1042 0.1; 1146 0.5; 1261 0.8; 1387 0.6; 1526 0.4; 1678 0.1; 1846 0.2; 2031 0.9; 2234 2.1; 2457 3.6; 2703 4.6; 2973 5.4; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.1; 6373 2.4; 7010 2.2; 7711 -3.7; 8482 -6.9; 9330 -6.0; 10263 -0.9; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -2.6; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T50p GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T50p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 25 Hz    |  0.98 | 6.5 dB   |
| Peaking | 168 Hz   |  3.99 | 5.6 dB   |
| Peaking | 355 Hz   |  0.95 | -5.4 dB  |
| Peaking | 4304 Hz  |  0.87 | 7.0 dB   |
| Peaking | 8616 Hz  |  3.32 | -10.1 dB |
| Peaking | 92 Hz    |  4.54 | -0.8 dB  |
| Peaking | 239 Hz   | 11.28 | 1.0 dB   |
| Peaking | 1882 Hz  |  4.12 | -1.7 dB  |
| Peaking | 2813 Hz  |  3.9  | 1.2 dB   |
| Peaking | 18352 Hz |  3.3  | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T50p/Beyerdynamic%20T50p.png)