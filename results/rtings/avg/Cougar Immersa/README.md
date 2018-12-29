# Cougar Immersa
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.6; 28 0.6; 31 -0.3; 34 -1.0; 37 -1.6; 41 -2.4; 45 -3.1; 49 -3.7; 54 -4.4; 60 -5.1; 66 -6.1; 72 -7.0; 79 -8.0; 87 -9.0; 96 -9.8; 106 -10.4; 116 -10.8; 128 -11.1; 141 -11.2; 155 -11.1; 170 -10.9; 187 -10.5; 206 -10.1; 227 -9.6; 249 -9.1; 274 -8.7; 302 -8.4; 332 -7.8; 365 -7.1; 402 -6.1; 442 -5.0; 486 -4.2; 535 -3.4; 588 -2.6; 647 -1.8; 712 -1.4; 783 -1.2; 861 -0.9; 947 -0.4; 1042 0.5; 1146 1.9; 1261 3.0; 1387 3.0; 1526 3.0; 1678 2.5; 1846 0.8; 2031 -1.0; 2234 -1.0; 2457 -0.0; 2703 0.6; 2973 0.4; 3270 -0.6; 3597 -2.6; 3957 -3.9; 4353 -4.2; 4788 -1.8; 5267 -1.8; 5793 -0.9; 6373 -2.1; 7010 -1.4; 7711 -3.0; 8482 -5.5; 9330 -5.4; 10263 -2.6; 11289 -1.1; 12418 -1.0; 13660 -1.2; 15026 -2.8; 16529 -3.9; 18182 -4.3; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cougar Immersa GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cougar Immersa ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 1.55 | 3.8 dB   |
| Peaking | 127 Hz   | 0.62 | -10.9 dB |
| Peaking | 304 Hz   | 1.28 | -4.3 dB  |
| Peaking | 8747 Hz  | 2.54 | -5.2 dB  |
| Peaking | 20364 Hz | 0.69 | -7.6 dB  |
| Peaking | 1422 Hz  | 2.11 | 4.0 dB   |
| Peaking | 2077 Hz  | 5.71 | -2.2 dB  |
| Peaking | 2880 Hz  | 4.71 | 1.3 dB   |
| Peaking | 4095 Hz  | 3.54 | -4.4 dB  |
| Peaking | 11851 Hz | 2.84 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cougar%20Immersa/Cougar%20Immersa.png)