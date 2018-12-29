# Sennheiser MM 550-X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.6; 116 5.4; 128 5.4; 141 5.4; 155 5.6; 170 5.8; 187 5.7; 206 5.7; 227 5.9; 249 6.0; 274 5.9; 302 5.9; 332 5.8; 365 5.4; 402 5.0; 442 4.6; 486 3.9; 535 3.1; 588 2.2; 647 1.4; 712 0.5; 783 -0.3; 861 -0.4; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.8; 1387 0.6; 1526 0.2; 1678 -0.9; 1846 -3.6; 2031 -7.0; 2234 -7.2; 2457 -3.9; 2703 -1.9; 2973 0.1; 3270 2.6; 3597 5.7; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 3.0; 7010 2.5; 7711 0.3; 8482 -2.5; 9330 -1.6; 10263 -0.1; 11289 -3.9; 12418 -5.6; 13660 -1.2; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MM 550-X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 550-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.16 | 6.1 dB  |
| Peaking | 321 Hz   | 1.08 | 3.8 dB  |
| Peaking | 2186 Hz  | 3.16 | -9.3 dB |
| Peaking | 4480 Hz  | 1.42 | 7.4 dB  |
| Peaking | 12031 Hz | 3.19 | -6.3 dB |
| Peaking | 821 Hz   | 3.82 | -1.7 dB |
| Peaking | 1398 Hz  | 3.45 | 1.1 dB  |
| Peaking | 5768 Hz  | 8.39 | 1.9 dB  |
| Peaking | 8709 Hz  | 5.33 | -3.9 dB |
| Peaking | 10174 Hz | 5.22 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20MM%20550-X/Sennheiser%20MM%20550-X.png)