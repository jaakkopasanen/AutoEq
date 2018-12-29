# Bowers & Wilkins P7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 -2.2; 23 -2.5; 25 -2.7; 28 -3.0; 31 -3.2; 34 -3.2; 37 -3.1; 41 -3.0; 45 -2.8; 49 -2.7; 54 -2.6; 60 -2.6; 66 -2.7; 72 -2.5; 79 -2.3; 87 -2.4; 96 -2.7; 106 -3.1; 116 -3.3; 128 -3.3; 141 -3.2; 155 -3.0; 170 -2.5; 187 -1.9; 206 -1.2; 227 -0.3; 249 0.5; 274 1.3; 302 1.7; 332 1.9; 365 1.5; 402 0.8; 442 0.5; 486 0.5; 535 0.5; 588 0.4; 647 0.4; 712 0.3; 783 0.2; 861 0.1; 947 -0.0; 1042 0.2; 1146 0.5; 1261 -0.2; 1387 -0.8; 1526 -1.6; 1678 -2.5; 1846 -3.2; 2031 -2.7; 2234 0.3; 2457 3.4; 2703 3.9; 2973 3.8; 3270 2.8; 3597 0.9; 3957 0.2; 4353 1.6; 4788 3.2; 5267 4.0; 5793 4.1; 6373 5.4; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -0.3; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.1; 16529 -2.0; 18182 -0.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bowers & Wilkins P7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers & Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.6  | -3.1 dB |
| Peaking | 128 Hz   | 1.97 | -3.1 dB |
| Peaking | 1917 Hz  | 2.9  | -5.0 dB |
| Peaking | 2645 Hz  | 2.47 | 5.2 dB  |
| Peaking | 5886 Hz  | 3.03 | 5.0 dB  |
| Peaking | 184 Hz   | 2.95 | -1.3 dB |
| Peaking | 312 Hz   | 1.85 | 2.3 dB  |
| Peaking | 1111 Hz  | 5.33 | 0.5 dB  |
| Peaking | 16438 Hz | 4.4  | -1.5 dB |
| Peaking | 16499 Hz | 2.54 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bowers%20&%20Wilkins%20P7/Bowers%20&%20Wilkins%20P7.png)