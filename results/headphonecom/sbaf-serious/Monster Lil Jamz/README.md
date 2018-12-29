# Monster Lil Jamz
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -9.4; 23 -9.3; 25 -9.2; 28 -9.0; 31 -8.9; 34 -8.7; 37 -8.6; 41 -8.4; 45 -8.3; 49 -8.2; 54 -8.0; 60 -7.9; 66 -7.8; 72 -7.7; 79 -7.6; 87 -7.5; 96 -7.4; 106 -7.1; 116 -7.0; 128 -6.8; 141 -6.6; 155 -6.5; 170 -6.2; 187 -5.9; 206 -5.6; 227 -5.2; 249 -4.9; 274 -4.4; 302 -3.9; 332 -3.4; 365 -2.9; 402 -2.5; 442 -2.1; 486 -1.6; 535 -1.1; 588 -0.6; 647 -0.1; 712 0.3; 783 0.4; 861 0.5; 947 0.2; 1042 -0.3; 1146 -0.8; 1261 -1.3; 1387 -1.0; 1526 -2.1; 1678 -2.8; 1846 -3.2; 2031 -3.4; 2234 -3.7; 2457 -3.5; 2703 -2.1; 2973 0.5; 3270 3.4; 3597 5.3; 3957 4.7; 4353 2.4; 4788 0.8; 5267 0.7; 5793 2.3; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -0.0; 15026 -1.2; 16529 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Lil Jamz GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Lil Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.25 | -8.9 dB |
| Peaking | 166 Hz   | 0.35 | -5.5 dB |
| Peaking | 1789 Hz  | 0.27 | 4.3 dB  |
| Peaking | 2160 Hz  | 0.87 | -8.4 dB |
| Peaking | 3572 Hz  | 3.19 | 6.5 dB  |
| Peaking | 752 Hz   | 5.3  | 0.4 dB  |
| Peaking | 5151 Hz  | 5.34 | -1.5 dB |
| Peaking | 6457 Hz  | 4.87 | 5.0 dB  |
| Peaking | 7891 Hz  | 1.68 | -1.6 dB |
| Peaking | 15087 Hz | 4.42 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Lil%20Jamz/Monster%20Lil%20Jamz.png)