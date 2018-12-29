# Sennheiser Game One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.5; 45 5.0; 49 4.6; 54 4.1; 60 3.5; 66 2.9; 72 2.4; 79 1.9; 87 1.3; 96 0.7; 106 0.2; 116 -0.3; 128 -0.8; 141 -1.1; 155 -1.3; 170 -1.4; 187 -1.4; 206 -1.3; 227 -1.1; 249 -1.1; 274 -1.1; 302 -1.1; 332 -1.1; 365 -1.0; 402 -1.0; 442 -1.1; 486 -1.1; 535 -0.9; 588 -0.8; 647 -0.6; 712 -0.1; 783 0.1; 861 0.1; 947 0.1; 1042 -0.0; 1146 0.1; 1261 -0.2; 1387 -0.3; 1526 0.1; 1678 -0.2; 1846 -0.5; 2031 -1.3; 2234 -1.6; 2457 -1.1; 2703 -0.7; 2973 -0.4; 3270 0.1; 3597 0.9; 3957 2.5; 4353 1.4; 4788 -0.1; 5267 1.5; 5793 1.6; 6373 0.1; 7010 -0.4; 7711 -0.5; 8482 -1.3; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.8; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Game One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Game One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.34 | 7.0 dB  |
| Peaking | 123 Hz  | 0.45 | -3.5 dB |
| Peaking | 2256 Hz | 3.4  | -1.6 dB |
| Peaking | 4015 Hz | 7.27 | 2.9 dB  |
| Peaking | 5578 Hz | 8.13 | 1.9 dB  |
| Peaking | 243 Hz  | 3.89 | 0.4 dB  |
| Peaking | 551 Hz  | 1.75 | -0.8 dB |
| Peaking | 773 Hz  | 1.51 | 0.6 dB  |
| Peaking | 8341 Hz | 5.4  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Sennheiser%20Game%20One/Sennheiser%20Game%20One.png)