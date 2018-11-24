# Sennheiser HD 212Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.9; 54 5.0; 60 3.9; 66 3.7; 72 3.2; 79 2.3; 87 1.6; 96 1.1; 106 0.7; 116 0.7; 128 1.7; 141 3.3; 155 2.8; 170 2.9; 187 3.1; 206 3.4; 227 3.8; 249 4.0; 274 4.1; 302 2.9; 332 2.5; 365 2.3; 402 2.8; 442 2.9; 486 2.6; 535 2.2; 588 1.8; 647 1.4; 712 0.8; 783 0.5; 861 0.6; 947 0.3; 1042 -0.3; 1146 -0.2; 1261 -0.1; 1387 -0.1; 1526 -0.4; 1678 -0.2; 1846 0.5; 2031 1.2; 2234 1.9; 2457 3.2; 2703 4.0; 2973 5.7; 3270 6.0; 3597 5.9; 3957 0.9; 4353 -0.6; 4788 2.0; 5267 4.8; 5793 6.0; 6373 4.4; 7010 1.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.2; 15026 -2.3; 16529 -1.3; 18182 -0.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 212Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 212Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.98 | 5.6 dB  |
| Peaking | 47 Hz    |  1.68 | 4.1 dB  |
| Peaking | 260 Hz   |  0.78 | 3.7 dB  |
| Peaking | 3109 Hz  |  3.06 | 6.5 dB  |
| Peaking | 5799 Hz  |  4.88 | 6.5 dB  |
| Peaking | 109 Hz   |  5.91 | -1.4 dB |
| Peaking | 491 Hz   |  4.73 | 0.9 dB  |
| Peaking | 3631 Hz  | 11.14 | 2.6 dB  |
| Peaking | 4224 Hz  |  8.23 | -3.3 dB |
| Peaking | 14814 Hz |  2.55 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20212Pro/Sennheiser%20HD%20212Pro.png)