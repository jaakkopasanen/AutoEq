# Sennheiser Game One

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.8; 41 5.3; 45 4.8; 49 4.3; 54 3.8; 60 3.3; 66 2.8; 72 2.4; 79 2.1; 87 1.7; 96 1.2; 106 0.6; 116 0.2; 128 -0.2; 141 -0.5; 155 -0.7; 170 -0.8; 187 -0.8; 206 -0.7; 227 -0.6; 249 -0.5; 274 -0.4; 302 -0.3; 332 -0.1; 365 0.1; 402 0.1; 442 -0.0; 486 0.1; 535 0.2; 588 0.3; 647 0.5; 712 0.7; 783 0.5; 861 0.3; 947 0.1; 1042 0.0; 1146 0.3; 1261 0.0; 1387 -0.3; 1526 -0.2; 1678 -0.5; 1846 -0.4; 2031 -0.8; 2234 -1.1; 2457 -0.6; 2703 0.1; 2973 1.1; 3270 2.6; 3597 4.1; 3957 4.9; 4353 2.7; 4788 1.5; 5267 4.5; 5793 5.5; 6373 3.9; 7010 2.3; 7711 0.3; 8482 -0.3; 9330 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.5  | 6.3 dB  |
| Peaking | 157 Hz  | 1.24 | -1.6 dB |
| Peaking | 3752 Hz | 2.68 | 7.3 dB  |
| Peaking | 4339 Hz | 0.83 | -3.4 dB |
| Peaking | 5820 Hz | 2.82 | 7.4 dB  |
| Peaking | 253 Hz  | 3.73 | -0.2 dB |
| Peaking | 721 Hz  | 1.89 | 0.7 dB  |
| Peaking | 2175 Hz | 7.44 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)