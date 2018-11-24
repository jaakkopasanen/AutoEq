# Sennheiser HD 598 CS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.4; 25 -1.6; 28 -1.8; 31 -2.0; 34 -2.0; 37 -2.1; 41 -2.1; 45 -2.1; 49 -2.0; 54 -1.9; 60 -1.7; 66 -1.6; 72 -1.6; 79 -1.3; 87 -1.2; 96 -1.2; 106 -1.0; 116 -0.9; 128 -1.2; 141 -1.5; 155 -1.9; 170 -1.8; 187 -0.8; 206 0.3; 227 1.5; 249 2.9; 274 4.0; 302 4.5; 332 4.3; 365 3.8; 402 3.1; 442 1.9; 486 1.4; 535 1.4; 588 1.3; 647 1.2; 712 0.9; 783 0.5; 861 0.1; 947 -0.0; 1042 0.1; 1146 0.2; 1261 0.5; 1387 0.8; 1526 1.0; 1678 1.1; 1846 1.1; 2031 1.3; 2234 1.8; 2457 2.9; 2703 4.4; 2973 4.6; 3270 2.5; 3597 2.2; 3957 4.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.8; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.4; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 598 CS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 CS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.59 | -2.1 dB |
| Peaking | 169 Hz   | 2.01 | -2.7 dB |
| Peaking | 305 Hz   | 1.38 | 5.0 dB  |
| Peaking | 2752 Hz  | 3.47 | 3.6 dB  |
| Peaking | 5081 Hz  | 1.81 | 6.7 dB  |
| Peaking | 1633 Hz  | 3.49 | 0.6 dB  |
| Peaking | 4168 Hz  | 8.46 | 2.2 dB  |
| Peaking | 6381 Hz  | 3.88 | 5.1 dB  |
| Peaking | 6543 Hz  | 1.42 | -3.2 dB |
| Peaking | 19741 Hz | 2.41 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20598%20CS/Sennheiser%20HD%20598%20CS.png)