# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.7; 87 5.3; 96 5.1; 106 4.8; 116 4.5; 128 4.3; 141 4.1; 155 4.1; 170 4.1; 187 4.1; 206 4.1; 227 4.3; 249 4.5; 274 4.6; 302 3.1; 332 2.4; 365 1.9; 402 1.2; 442 0.6; 486 0.2; 535 0.1; 588 0.4; 647 0.8; 712 0.8; 783 0.5; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 0.1; 1387 -0.2; 1526 -1.4; 1678 1.9; 1846 -0.6; 2031 -1.3; 2234 -0.8; 2457 0.7; 2703 1.7; 2973 1.3; 3270 0.0; 3597 -0.2; 3957 2.1; 4353 6.0; 4788 6.0; 5267 1.8; 5793 4.7; 6373 3.0; 7010 0.9; 7711 -1.1; 8482 -2.1; 9330 -1.5; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 201 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.24 | 6.2 dB  |
| Peaking | 253 Hz   | 2.31 | 2.8 dB  |
| Peaking | 4531 Hz  | 4.81 | 6.6 dB  |
| Peaking | 6068 Hz  | 5.47 | 4.2 dB  |
| Peaking | 8501 Hz  | 4.06 | -2.7 dB |
| Peaking | 494 Hz   | 5.06 | -0.8 dB |
| Peaking | 2125 Hz  | 4.87 | -2.2 dB |
| Peaking | 2792 Hz  | 2.33 | 2.0 dB  |
| Peaking | 3445 Hz  | 5.47 | -2.4 dB |
| Peaking | 10611 Hz | 3.56 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)