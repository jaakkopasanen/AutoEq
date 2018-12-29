# Obravo HAMT1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.7; 31 3.7; 34 2.9; 37 2.4; 41 2.1; 45 1.7; 49 0.9; 54 -1.2; 60 -4.4; 66 -6.2; 72 -7.7; 79 -9.2; 87 -10.5; 96 -11.3; 106 -11.6; 116 -11.1; 128 -10.2; 141 -8.9; 155 -7.4; 170 -5.7; 187 -4.4; 206 -2.4; 227 -0.0; 249 2.6; 274 5.8; 302 6.0; 332 6.0; 365 5.5; 402 0.6; 442 -3.3; 486 -7.6; 535 -10.3; 588 -9.1; 647 -7.0; 712 -5.2; 783 -3.4; 861 -2.1; 947 -0.8; 1042 0.6; 1146 2.3; 1261 3.9; 1387 5.2; 1526 6.0; 1678 6.0; 1846 3.9; 2031 -2.8; 2234 -3.6; 2457 -1.7; 2703 -1.4; 2973 -2.2; 3270 -3.1; 3597 -3.4; 3957 -2.9; 4353 -1.4; 4788 1.6; 5267 3.6; 5793 3.9; 6373 4.4; 7010 2.5; 7711 0.1; 8482 -5.4; 9330 -8.2; 10263 -6.4; 11289 -1.8; 12418 0.0; 13660 -0.7; 15026 -3.0; 16529 -3.7; 18182 -4.5; 20000 -5.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Obravo HAMT1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Obravo HAMT1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 111 Hz   | 1.17 | -12.8 dB |
| Peaking | 323 Hz   | 1.78 | 11.6 dB  |
| Peaking | 540 Hz   | 1.91 | -12.8 dB |
| Peaking | 1462 Hz  | 3.17 | 7.6 dB   |
| Peaking | 22076 Hz | 0.12 | -4.6 dB  |
| Peaking | 25 Hz    | 1.28 | 6.8 dB   |
| Peaking | 2168 Hz  | 7.08 | -6.0 dB  |
| Peaking | 3770 Hz  | 1.32 | -11.4 dB |
| Peaking | 5740 Hz  | 0.57 | 11.3 dB  |
| Peaking | 9204 Hz  | 2.54 | -13.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Obravo%20HAMT1/Obravo%20HAMT1.png)