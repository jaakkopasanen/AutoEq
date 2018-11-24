# Beyerdynamic DT 235

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.7; 41 4.8; 45 3.9; 49 3.1; 54 2.2; 60 1.5; 66 0.9; 72 0.2; 79 -0.3; 87 -0.4; 96 -0.8; 106 -1.5; 116 -1.8; 128 -2.1; 141 -2.2; 155 -2.1; 170 -1.9; 187 -1.6; 206 -0.8; 227 -0.5; 249 -0.6; 274 -0.6; 302 -0.5; 332 -0.6; 365 -0.8; 402 -0.9; 442 -0.5; 486 -0.5; 535 -0.3; 588 0.1; 647 -0.2; 712 -0.8; 783 -1.0; 861 -1.2; 947 -0.5; 1042 -0.1; 1146 0.1; 1261 0.5; 1387 0.2; 1526 -2.7; 1678 -4.5; 1846 -3.4; 2031 -1.3; 2234 0.3; 2457 2.0; 2703 2.8; 2973 4.6; 3270 5.1; 3597 3.4; 3957 5.8; 4353 2.2; 4788 -3.9; 5267 -1.9; 5793 2.9; 6373 5.1; 7010 2.5; 7711 -1.3; 8482 -6.0; 9330 -6.9; 10263 -3.8; 11289 -0.2; 12418 0.0; 13660 -1.7; 15026 -2.8; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 235 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 235 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 1.43 | 7.2 dB  |
| Peaking | 1729 Hz  | 4.22 | -5.2 dB |
| Peaking | 3227 Hz  | 2.53 | 5.8 dB  |
| Peaking | 6538 Hz  | 5.88 | 6.5 dB  |
| Peaking | 9026 Hz  | 3.16 | -7.9 dB |
| Peaking | 138 Hz   | 1.57 | -2.5 dB |
| Peaking | 456 Hz   | 0.9  | -0.5 dB |
| Peaking | 4112 Hz  | 8.14 | 4.4 dB  |
| Peaking | 4816 Hz  | 7.08 | -5.7 dB |
| Peaking | 14732 Hz | 6.85 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20235/Beyerdynamic%20DT%20235.png)