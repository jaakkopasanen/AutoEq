# Signature Acoustics Elements C12

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 -7.6; 23 -8.2; 25 -8.6; 28 -9.2; 31 -9.7; 34 -10.2; 37 -10.6; 41 -11.0; 45 -11.4; 49 -11.7; 54 -12.1; 60 -12.6; 66 -12.9; 72 -13.3; 79 -13.7; 87 -14.1; 96 -14.6; 106 -14.7; 116 -14.8; 128 -15.0; 141 -15.1; 155 -15.1; 170 -15.0; 187 -14.8; 206 -14.5; 227 -14.1; 249 -13.7; 274 -13.2; 302 -12.5; 332 -11.9; 365 -11.2; 402 -10.4; 442 -9.4; 486 -8.6; 535 -7.6; 588 -6.3; 647 -5.1; 712 -4.1; 783 -2.8; 861 -1.7; 947 -0.6; 1042 0.4; 1146 1.4; 1261 2.2; 1387 1.5; 1526 -0.5; 1678 -1.9; 1846 -2.4; 2031 -2.7; 2234 -2.2; 2457 -0.7; 2703 0.7; 2973 2.3; 3270 3.3; 3597 3.0; 3957 0.9; 4353 -2.6; 4788 -5.2; 5267 -7.1; 5793 -9.5; 6373 -7.7; 7010 -4.3; 7711 -2.3; 8482 -2.4; 9330 -4.2; 10263 -4.2; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -5.3; 18182 -6.3; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Signature Acoustics Elements C12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Signature Acoustics Elements C12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 60 Hz    | 0.3  | -11.0 dB |
| Peaking | 185 Hz   | 0.7  | -7.9 dB  |
| Peaking | 398 Hz   | 1.33 | -5.1 dB  |
| Peaking | 5895 Hz  | 3.09 | -10.0 dB |
| Peaking | 17829 Hz | 2.04 | -7.3 dB  |
| Peaking | 1231 Hz  | 1.85 | 6.4 dB   |
| Peaking | 2963 Hz  | 0.44 | -6.8 dB  |
| Peaking | 3287 Hz  | 1.78 | 10.4 dB  |
| Peaking | 9276 Hz  | 0.87 | 5.0 dB   |
| Peaking | 9736 Hz  | 3.07 | -7.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Signature%20Acoustics%20Elements%20C12/Signature%20Acoustics%20Elements%20C12.png)