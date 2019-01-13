# SMS Audio STREET by 50 Active Noise Cancelling
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 4.8; 34 2.3; 37 -0.8; 41 -4.1; 45 -6.2; 49 -6.7; 54 -6.3; 60 -5.3; 66 -4.2; 72 -3.4; 79 -2.5; 87 -1.8; 96 -1.5; 106 -1.2; 116 -1.0; 128 -0.5; 141 0.0; 155 0.5; 170 1.1; 187 1.6; 206 2.1; 227 2.6; 249 3.0; 274 3.2; 302 3.4; 332 3.6; 365 4.4; 402 4.7; 442 5.1; 486 5.4; 535 5.4; 588 5.3; 647 4.9; 712 4.1; 783 2.9; 861 1.7; 947 0.5; 1042 0.0; 1146 -0.1; 1261 -1.2; 1387 -0.6; 1526 -0.1; 1678 0.1; 1846 1.7; 2031 3.4; 2234 4.0; 2457 3.9; 2703 3.3; 2973 3.7; 3270 5.2; 3597 5.8; 3957 5.7; 4353 6.0; 4788 6.0; 5267 5.2; 5793 1.0; 6373 0.3; 7010 0.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -3.0; 13660 -7.4; 15026 -6.0; 16529 -3.6; 18182 -0.1; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS Audio STREET by 50 Active Noise Cancelling GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS Audio STREET by 50 Active Noise Cancelling ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.95 | 10.6 dB  |
| Peaking | 46 Hz    | 1.2  | -12.0 dB |
| Peaking | 440 Hz   | 0.94 | 5.6 dB   |
| Peaking | 3905 Hz  | 1.35 | 6.4 dB   |
| Peaking | 14315 Hz | 2.28 | -8.0 dB  |
| Peaking | 677 Hz   | 2.54 | 2.3 dB   |
| Peaking | 1555 Hz  | 0.73 | -3.1 dB  |
| Peaking | 2140 Hz  | 2.27 | 4.4 dB   |
| Peaking | 5093 Hz  | 5.45 | 3.3 dB   |
| Peaking | 5921 Hz  | 4.18 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling/SMS%20Audio%20STREET%20by%2050%20Active%20Noise%20Cancelling.png)