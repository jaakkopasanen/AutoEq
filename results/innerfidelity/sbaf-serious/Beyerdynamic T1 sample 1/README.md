# Beyerdynamic T1 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.2; 28 4.6; 31 4.2; 34 3.8; 37 3.4; 41 3.1; 45 2.7; 49 2.4; 54 2.5; 60 2.9; 66 1.9; 72 1.1; 79 0.5; 87 0.0; 96 -0.5; 106 -0.9; 116 -1.1; 128 -1.4; 141 -1.7; 155 -1.9; 170 -2.0; 187 -2.1; 206 -2.2; 227 -2.2; 249 -2.2; 274 -2.1; 302 -2.1; 332 -1.9; 365 -1.8; 402 -1.7; 442 -1.4; 486 -1.2; 535 -1.1; 588 -0.8; 647 -0.6; 712 -0.7; 783 -0.2; 861 -0.2; 947 0.0; 1042 0.1; 1146 0.4; 1261 0.6; 1387 0.5; 1526 -0.6; 1678 -1.6; 1846 -1.8; 2031 0.0; 2234 1.7; 2457 -0.4; 2703 0.2; 2973 0.5; 3270 1.4; 3597 1.0; 3957 0.9; 4353 0.0; 4788 3.6; 5267 5.5; 5793 -3.2; 6373 -5.3; 7010 -2.2; 7711 -7.7; 8482 -12.4; 9330 -10.7; 10263 -3.4; 11289 0.0; 12418 0.0; 13660 -0.2; 15026 -1.8; 16529 -2.0; 18182 -0.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic T1 sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 18 Hz    |  0.61 | 6.0 dB   |
| Peaking | 60 Hz    |  3.3  | 1.7 dB   |
| Peaking | 205 Hz   |  0.56 | -2.5 dB  |
| Peaking | 5078 Hz  |  8.68 | 7.8 dB   |
| Peaking | 8619 Hz  |  3.35 | -13.6 dB |
| Peaking | 1758 Hz  |  5.4  | -3.1 dB  |
| Peaking | 2441 Hz  |  0.58 | 1.1 dB   |
| Peaking | 6137 Hz  | 11.27 | -5.8 dB  |
| Peaking | 11365 Hz |  5.02 | 2.7 dB   |
| Peaking | 16022 Hz |  3.48 | -2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sample%201/Beyerdynamic%20T1%20sample%201.png)